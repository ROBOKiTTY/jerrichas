# Jerrichas by Jerricha@chat.cohtitan.com, Summer 2015!
# GPLv3

from .base import BaseCostumeSave
import csv

class CostumeCSV(BaseCostumeSave):
    """
    Represents a file produced with the /costumesave command in Icon.exe

    :param fp: a /costumesave CSV file
    :type fp: file
    """

    def get_costumeparts(self):
        """
        :returns: a mapping of /costumesave elements to ParagonChatDB 'costumepart' columns
        """
        super()
        self.fp.seek(0)
        costume_csv = csv.reader(self.fp)
        costume = map(
            lambda row: dict(
                part=row[0],
                geom=row[1],
                tex1=row[2],
                tex2=row[3],
                fx=row[39] if not row[39]=="0" else "",
                displayname=row[4],
                region=row[42],
                bodyset=row[43],
                # name=row[],
                color1=row[5],
                color2=row[6],
                # color3=row[],
                # color4=row[],
            ),
            costume_csv
        )
        self.fp.seek(0)
        return list(costume)

    def get_scales(self):
        """
        :returns: a mapping of /costumesave records to ParagonChatDB 'costume' columns.
        """
        super()
        self.fp.seek(0)
        int_convert = lambda x, y, z: int(float(z) * 100) << 16 | int(float(y) * 100) << 8 | int(float(x) * 100)

        row = csv.reader(self.fp).__next__()
        proportions = dict(
            ## Atomic ##
            bodytype=row[7],
            skincolor=row[8],  # Conversion may be required
            bodyscale=row[9],
            bonescale=row[10],
            shoulderscale=row[12],
            chestscale=row[13],
            waistscale=row[14],
            hipscale=row[15],
            legscale=row[16],

            ## Head/Face Scales (Composites) ##
            headscales=int_convert(*row[18:20+1]),
            browscales=int_convert(*row[21:23+1]),
            cheekscales=int_convert(*row[24:26+1]),
            chinscales=int_convert(*row[27:29+1]),
            craniumscales=int_convert(*row[30:32+1]),
            jawscales=int_convert(*row[33:35+1]),
            nosescales=int_convert(*row[36:38+1]),
        )
        return proportions
