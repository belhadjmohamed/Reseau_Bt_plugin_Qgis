# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Reseau_BT
                                 A QGIS plugin
 Reseau_BT
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-04-12
        copyright            : (C) 2023 by Reseau_BT
        email                : bemoh70@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Reseau_BT class from file Reseau_BT.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Reseau_BT import Reseau_BT
    return Reseau_BT(iface)
