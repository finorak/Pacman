# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    __init__.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: nyramana <nyramana@student.42antananariv  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/19 10:46:37 by nyramana         #+#    #+#              #
#    Updated: 2026/08/19 10:46:37 by nyramana        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

"""Package that contain the rendering part of the program."""

from .core import XMain
from .rendering import Rendering

__all__ = ["Rendering", "XMain"]
