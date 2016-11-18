# coding: utf-8

import xml.etree.ElementTree as et
import os

import pdb

class mgr_param:

    def __init__(self, path='param.xml'):
        """constructeur"""

        self._path_param = path
        self._path_music = ''

        self.import_param()


    def __str__(self):
        """conversion en string"""
        return ("PARAMETRE:\n" +
                "\tpath music: {}\n".format(self._path_music))

        return None

    def set_path_music(self, path):
        self._path_music = path


    def import_param(self):
        """Importer les données de configuration"""

        try:

            tree = et.parse(self._path_param)
            root = tree.getroot()
            children = root.getchildren()

            # récupération path_music
            for child in children:

                if child.tag == 'path_music':
                    if child.text is not None:
                        self._path_music = child.text

        except IOError as err:
            print(err.message)

        return None

    def export_param(self):
        """
            Exporter les données de configuration

            return  True:   Fichier exporté correctement
                    False:  Erreur durant l'écriture du fichier

        """

        # création de la racine
        root = et.ElementTree(None, None)
        racine = et.Element("param")

        # param path_music
        music_element = et.Element("path_music")
        music_element.text = self._path_music
        racine.append(music_element)

        root._setroot(racine)

        try:
            root.write(self._path_param)
            return True

        except PermissionError as err:
            print(err.message)
            return False

        self._path_music = path
