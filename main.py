# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    main.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: nyramana <nyramana@student.42antananariv  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/19 14:35:18 by nyramana         #+#    #+#              #
#    Updated: 2026/08/19 14:36:10 by nyramana        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from src.rendering import Rendering


def main() -> None:
    rendering = Rendering((1400, 1000))
    rendering.run()


if __name__ == "__main__":
    main()
