# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    game.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: nyramana <nyramana@student.42antananariv  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/19 10:48:47 by nyramana         #+#    #+#              #
#    Updated: 2026/08/19 10:48:47 by nyramana        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from ..core import XMain
from .base import Screen


class Game(Screen):
    def __init__(self, xmain: XMain) -> None:
        super().__init__(xmain)

    def get_input(self, key: int, _) -> str | None: ...

    def update(self, dt: float) -> None: ...

    def render(self) -> None: ...
