from .core import ImgData, XMain


class Image:
    def __init__(self, xmain: XMain) -> None:
        self.xmain = xmain

    def get_pixel(self, img: ImgData, pos: tuple[int, int]) -> int:
        bytes_per_pixel = img.bpp // 8
        if bytes_per_pixel != 4:
            raise RuntimeError(f"Unsupported pixel format: {img.bpp} bpp")

        if 0 <= pos[0] < img.width and 0 <= pos[1] < img.height:
            offset = pos[1] * img.sl + pos[0] * bytes_per_pixel
            return int.from_bytes(
                bytes(img.data[offset : offset + bytes_per_pixel]),
                "little" if img.endian == 0 else "big",
            )
        return 0

    def put_pixel(
        self,
        img: ImgData,
        pos: tuple[int, int],
        color: int,
    ) -> None:
        bytes_per_pixel = img.bpp // 8
        if bytes_per_pixel != 4:
            raise RuntimeError(f"Unsupported pixel format: {img.bpp} bpp")

        if 0 <= pos[0] < img.width and 0 <= pos[1] < img.height:
            offset = pos[1] * img.sl + pos[0] * bytes_per_pixel
            img.data[offset : offset + bytes_per_pixel] = int(color).to_bytes(
                bytes_per_pixel,
                "little" if img.endian == 0 else "big",
            )

    def draw_line(
        self,
        img: ImgData,
        start: tuple[int, int],
        end: tuple[int, int],
        thickness: int = 1,
        color: int = 0xFFFFFFFF,
    ) -> None:
        # Bresenham's line algorithm + Thickness

        dx = abs(end[0] - start[0])
        dy = abs(end[1] - start[1])
        sx = 1 if start[0] < end[0] else -1
        sy = 1 if start[1] < end[1] else -1
        err = dx - dy

        x, y = start[0], start[1]

        while True:
            for dx_thick in range(-thickness // 2, thickness // 2 + 1):
                for dy_thick in range(-thickness // 2, thickness // 2 + 1):
                    self.put_pixel(img, (x + dx_thick, y + dy_thick), color)

            if x == end[0] and y == end[1]:
                break

            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy

    def copy_sprite(
        self,
        src: ImgData,
        dest: ImgData,
        size: tuple[int, int],
        pos: tuple[int, int],
    ) -> ImgData:
        sy = 0
        while sy < size[1]:
            sx = 0
            while sx < size[0]:
                color = self.get_pixel(src, (pos[0] + sx, pos[1] + sy))
                self.put_pixel(dest, (sx, sy), color)
                sx += 1
            sy += 1
        return dest

    def generate_image(self, size: tuple[int, int]) -> ImgData:
        img_data = ImgData()
        tmp = self.xmain.mlx.mlx_new_image(
            self.xmain.mlx_ptr, size[0], size[1]
        )
        if not tmp:
            raise RuntimeError("Cannot initialize cell Image")
        img_data.width, img_data.height = size
        img_data.img = tmp
        img_data.data, img_data.bpp, img_data.sl, img_data.endian = (
            self.xmain.mlx.mlx_get_data_addr(tmp)
        )
        img_data.data[:] = b"\x00" * len(img_data.data)
        return img_data
