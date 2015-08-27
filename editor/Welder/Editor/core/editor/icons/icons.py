import wx
#from wx.lib.embeddedimage import PyEmbeddedImage
import Kernel

from GenImages import catalog


class IconManager(object):

    _catalog = catalog

    @staticmethod
    def getIcon(name):
        if name in IconManager._catalog:
            wx.Log.EnableLogging(False)
            return IconManager._catalog[name].GetIcon()
            wx.Log.EnableLogging(True)
        else:
            Kernel.Log(
                "Warning: Icon '%s' requested but not found, "
                "Loading empty bitmap insted" % name,
                "[IconManger]"
            )
            empty_bitmap = wx.Bitmap(16, 16)
            return wx.Icon(empty_bitmap)

    @staticmethod
    def getBitmap(name):
        if name in IconManager._catalog:
            wx.Log.EnableLogging(False)
            return IconManager._catalog[name].GetBitmap()
            wx.Log.EnableLogging(True)
        else:
            Kernel.Log(
                "Warning: Bitmap '%s' requested but not found, "
                "Loading empty bitmap insted" % name,
                "[IconManger]"
            )
            return wx.Bitmap(16, 16)

    @staticmethod
    def getImage(name):
        if name in IconManager._catalog:
            wx.Log.EnableLogging(False)
            return IconManager._catalog[name].GetImage()
            wx.Log.EnableLogging(True)
        else:
            Kernel.Log(
                "Warning: Image '%s' requested but not found, "
                "Loading empty bitmap insted" % name,
                "[IconManger]"
            )
            return wx.Image(16, 16)

    @staticmethod
    def Names():
        return list(IconManager._catalog.keys())


# #==============================================================================
# # * BEGIN Icon Embeding
# #==============================================================================

# arcicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAABrFJ"
#     "REFUWIXlV2lQVecZfr5zLnflcoHLcgNIZFyCUqmloCzGlEpiIlKc1K0kpqLGqdalBqia2kSb"
#     "oAEnGbKYzbjEXIjGtOIkYWxM0iJOwQQNRIyAguzIctdzD+fes/aHIliM/SOZzvSZ+X6c877f"
#     "eZ55zzvP+33A/zvo8SYIOTYtXunN/J1T0C95JzU74YRulc/a/1n3cFw1nuRp+YfXr9BPfV0u"
#     "APW+AuyEBG72IoIInBvOIeNFnmvdZZoT8mifl5M0hAKcLNefkrsnL933RSkAZThv3CrwN1tO"
#     "dGqQTSPLCghFBl07c6an+/ps/5lHjZeAD1/YEi5JMiRJAk0pptDr+RYAeOOVl+jItQdXh66r"
#     "yB5XAfcP1j/h9YkQRRkcK/pprQ+evWpK2RuY+kTNhoei9tvD43qAH+iBn6XPmNDOGMLstTXn"
#     "7xSfMu2+xK36by2SdOOZpgHD8t+zjrbi2vX7JjEL9l1aPi+0v4znFAIAgkxA/DQgCgVCE/ho"
#     "bXN0cXheW47VNkbAR1Vro+q11jqOcQf1/6H5cet300+Ojmem7TDHv1LU6rruCxj9Xq0BiE7N"
#     "LF3/3NtVz8/dwHsEnaIArH8EWNMkEEkNURzJV+mBOe97No35BYF58dtc/W4z5wIVW55ZePVc"
#     "wm05OwKT/uixeQNkUcbo5WVlcINe49GSrQUOt6LjBQlufRiGTA9AYFXgvSO5iiyD1wV0vPPl"
#     "9+/eVoH3MpZZavNLr3EDshYA1Cag+re1ixocqScBwNlVSoqmSNt7m1g95FEbaUC+vGO26GjN"
#     "0NF6aLkmCD0NijxtARFZLVi12hEy/08fcPYoBjKgMgJZ1UmV2QsTT98m4MCk0r2nn3s838sr"
#     "kGRF0lEUHZGcXF0yoz71Tr0wjLc1L89ufy3uVKdkCRSNsfAxrWxE7JxDtp6eDUOioCz+5YqU"
#     "p6LLz91p7y0rLtlPmz9Pt1q9Dl7tDp5ebUjo+MzXkp7k6F41QWpu+qfDdrn96+ObSZw/FTXj"
#     "WkhAmtYSkKa1BJxYqk4+9psVnzhdoonRxsDnU0M9e8OJebtqvquL4R+VTRMai1Prn/0h8beM"
#     "yL3u2CbPiy5/nwTQe5YXxj/010unLX9eo1fgl/pWz7aWeah8rG6LIXGaqtOvYKRwqwHAB/A0"
#     "BdkOCCoOruTTFY3hDhM3j4IhiBbuVj0KAJatzQ2oevHBjZLTCZcUcuHv3zxSsev11jYlakmp"
#     "xDHoOmOd/6vlrpkDxyvh9XBg3a4xS3A64B1i0MPFfK58GlnWHbm3RfQwcDd9E1fW0Tb1rhVI"
#     "KJy17tTu1iBeBIxzD++roJm8L5U9KC//0HuRs4NIPDEvztqKNd6nUXEUsizD1tsOSvICNA1F"
#     "G4KQAD1Ufhoc+nr6m3NeqBU/rredWfie2+VPGNPBdyO+eKm98K0Z0WYGw91LqXCerO8g/NYp"
#     "+izhYCvv7gy3i9EN2WuKPq76YOVOCOyITAJAHSxdTIpPjDtX9y1FFGj4Tuh1FPoGB7sGQku2"
#     "B7gO7DeqWa3KYHHm+2fNmr+buzKr+Bf56qaNe/0w6ls3xxAPAzypnU+Sl6tnbTrx6uJXRUmG"
#     "Mnn3Wl1v0R6R7TePzKuboDUwGIMaPR4mlhACrUqEi3G3RaZ/lVG+ubol8dnIVVTTxgNqWoLB"
#     "PPH77afo5OQrkZ6EXP9iP8cnWww6QlOQbwggFJxCWEP9UutM1cmKa5c72J+sIH5m2Xr06tmn"
#     "fjqTk/gxQwuhOFPAewbiBR8PQlNwCtIVyyP/yijffKEDAGp3dx+cnLuun++rCqSlQOiUxfdp"
#     "VdebARRkHbG/ebHCliS7r6gBGaANmLjwfD2dUyWRS0uq/jLU3G28W6fWHC+KqS0vyZZveinP"
#     "80h78vmPUn79TM/d9v03qCdHMiTzjV6FsON+MrsjJL0EVWud5xCYllsV8PaeTTTqpIk+QYYo"
#     "CBjuGkJoeCV1ozFqbsO9EqAYYphbjuLZ0k8tc5Yd6Go5vxKyBEUZMXtKpYbd7qgmwc8saK9M"
#     "d94rAcAoJ3yaVG3rbqld6bb3QavVQ1FuDHuVnxZ2m62KC16WaatMZ+4lOXBzFhypKzYcLjzy"
#     "qcvp/GrQ5lutVlPBNK3ECj4WkiSDVVIyBi/kXb/X5MDIiYgC/M2AZwAAjBGLpoYEOppEngVR"
#     "6Ts7Gs9Ejwf5TWIAgDxMDgBlNa2syA/JsiTA52Vqx4t8DLghhjzw88dyLPfHdYVFTlGCwiaK"
#     "tCbs4R9NQEjEpKV6o9mpM5icOv/gfwCa+T8a+SgQjOON6X8O/wZH5RXGaPlomgAAAABJRU5E"
#     "rkJggg==")
# IconManager._catalog['arcicon'] = arcicon


# #----------------------------------------------------------------------
# actorsicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAAd0SU1FB9sKFgQ5OzNpmuwAAAAZ"
#     "dEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAAA7ElEQVQ4y5WTMQrCMBSGv6on"
#     "cHMXAuLiKA4OBXFtg3gAFy+gaxcnT9AjdKnu7uIsFMETdPMKz0EDTW00/hBe8if/z3svCThw"
#     "mCGHGcIPtFziKNZeRi2nuCwAiGJNNFa4TIJvYoDj5Y7hjpc78cnWdOqOj93VJgYVbuDZgyqm"
#     "tz7dVRsvSKIEEDnv7ZjqV3ztu3tgfOS8/2zWZNt4PnAlUzVxiRuFgGzmIzHzhrVbLImq12ut"
#     "zfyvW/BGFmKlXc/AjPe55gwkUUiqycIKWRZkIUiqkUT9fkjBOme50Ba3XGiCde7/GykL6A29"
#     "Sn8CmvqDA2GZ0QUAAAAASUVORK5CYII=")
# IconManager._catalog['actorsicon'] = actorsicon


# #----------------------------------------------------------------------
# animationsicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAAd0SU1FB9sKFgUFIiUzIeQAAAAZ"
#     "dEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAAAoUlEQVQ4y2P8//8/AyWACZug"
#     "8ibf/8SKMxFrk/Im3/+TTS9iGvL//38UrLTR5//WZ7L/lTb6/Mcmhy7GhM+J6Py7fpsZ0V3G"
#     "+P//f7jCyaYXMZyee1ofp2a4Aeg2Tja9SFAj1kBEV4xPM9x76IGCK7BwYSZSEg22dMBIbErc"
#     "9lwOrtBL8hEjSQkJX/QyEZOE8QYuMSkQX+CSHfowzEhpdgYAhAT7IDPeL2kAAAAASUVORK5C"
#     "YII=")
# IconManager._catalog['animationsicon'] = animationsicon


# #----------------------------------------------------------------------
# armorsicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAAd0SU1FB9sKFgUBHxk3qPEAAAAZ"
#     "dEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAABJUlEQVQ4y6WSMW4CMRRE30f0"
#     "qZYqosslbG25ZbhFuu1Jh+hyALrcIim3tPAl6CKqbJUTTApi410WKDLSl+yx/tf8GSMJSTjn"
#     "BORKvCRK3jk3eJsDeO8VY2Sz2QBQVRVmJklmZir5tm3x3mu/3xvAzHuvpmko0fc9u92OsrlE"
#     "0zR47wUw45+YAXRdhyTbbrcDqSEEEgfQti2SrOu6zNmfSWfCTAAhhMzVdQ0nZ21SwRipeb1e"
#     "Mx52gTKSFFkIQc45hRAG0Y4rx3gNdV3zRpXvH+6JVTwM1p1PKLLkQ8LL48NpQHF+P/5c90CS"
#     "TRk2hYsUxok4566+xxhvewCwiocs+3m54PPrO68Q4faA7MfxvHtqfqVHkt1VUA5huRg03/Vg"
#     "6oeOf+QvByXDHWBPam8AAAAASUVORK5CYII=")
# IconManager._catalog['armorsicon'] = armorsicon

# #----------------------------------------------------------------------
# classesicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAAd0SU1FB9sKFgQ6IJIhAMMAAAAZ"
#     "dEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAABzUlEQVQ4y32TvWtTYRjFf4/c"
#     "JCQgTZRqKCEdTNGCZpCCpjQhm0NEUJO1CE4hIOiia7N0cyiBbhJKVgWH/At1URy0NCAuuUs1"
#     "hGYSTArHIbm3t/nwhRfej+ec5/OYJADMbHyYLEnGghW0dbyHZrXE5WgEgO/d35iZ5pGYmWq1"
#     "Go1GAzPDiUVCPvjI7SGJ2+lr7JS3ZkiCYNd1zyPwwLsfPwHw5tF9VpeX5nrO5XK4rks6nUaS"
#     "XQoa3bieAOCb2wOgXsljZgqCC4WCDwZw/vwdWSwS0v7zB9xauQJA++tPAB7ezQCwCOxVm0kn"
#     "FA07ioYdeXdAtVpNrVZL3W5XY3MR3L6ht4OEHrjT6cwFSxoX8XHhC6eDExLxpN/j6bCb1dLc"
#     "1trEM8VsG4BEPMnKnXcXwAA75S1Wl5d4tt9eXINitq2Tl6/VT2Vmci7fu6l6Ja9mtXQx1WmC"
#     "fiqjfiqjzfWDmbwB1St5vX/1xP8zSZiZNtcPCIeuMhz1GZ4NCDtxhmcDPv94wfQ0epP79O0H"
#     "HDNTMdsmEU/yq3fE4fE2ABtre4Sd+IyQJJlH4o/ycNTndACHx9u+NzPTxtreXDVKslgkpGjY"
#     "OU9hWsJByf5P2v8AIeU7AH0L6xwAAAAASUVORK5CYII=")
# IconManager._catalog['classesicon'] = classesicon

# #----------------------------------------------------------------------
# commoneventsicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAAd0SU1FB9sKFgUHAMJlAoIAAAAZ"
#     "dEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAABMUlEQVQ4y42TMU7DQBBF30aR"
#     "3NkHQGmQ5Qs4pkMUNBRI1BwhZVCo0rihAsllKq6AhESRxkVEGXIBK6KJ6HE6V0OBdlnvriW+"
#     "tIVnd/7MH/9RIoILpZQfBEREubFxKHmxbMz3dnekyGNz55Io3YGuenH14VU+zEoAuqbl6/69"
#     "183IfnjyeD6YDBBlifdmrKufvl4DsGcOQFpXpmqUJR6JljOyk/UDG2ldMVmVDMFI6JrWnBAm"
#     "q7J3t1g2KKVkpJN1y3b7Luz4dnf8HT4gockD7C/ng6RFHvP0kP1JsKetcfv9TJQlRFnSI+v5"
#     "4D8dhCRt1lNERCkRMe7TuobI0rriMCuNoQyB64XQbyvymJezu16y58TPmze6ph3Ua1vZ2wV3"
#     "E925bNbT4Eaq0DqHVjq0ygA/Y4WmG9536uEAAAAASUVORK5CYII=")
# IconManager._catalog['commoneventsicon'] = commoneventsicon


# #----------------------------------------------------------------------
# copyicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAAd0SU1FB9sKFgQ3JCDiupcAAAAZ"
#     "dEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAABAElEQVQ4y2NkQAItQeb/GfCA"
#     "mnUnGdHFWJA1Z0+qZGBgYGD48ekqw9dnagwMDAwMHx7eZNixdTNDcosfAwMDw390Q1jQTRSY"
#     "XY7CPysXy8DAwAA3EKcLYOBDaieqgTd+MzAwbGb48PAmYQN+fLrKILFyEYqCH+FxDAwMDAw7"
#     "tm7GGgaMyGEQkVXCIKzBCpecmtfOQChQcYZB62UBBmIClQU5+lZM62FgYBAgKVBZsEUfzBZi"
#     "ApUFnx+JCVQWSMi2Y02BX5+pobjgx6erGKmSBVcShYULehjctW3Bn5AIBaqH3E38BuAL1OxJ"
#     "lQx3d15BUc/EQAJ4e+M3A86USG62BgBGopePASKOEQAAAABJRU5ErkJggg==")
# IconManager._catalog['copyicon'] = copyicon

# #----------------------------------------------------------------------
# dimlayersofficon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAACXBIWXMAAAsTAAALEwEAmpwY"
#     "AAAKT2lDQ1BQaG90b3Nob3AgSUNDIHByb2ZpbGUAAHjanVNnVFPpFj333vRCS4iAlEtvUhUI"
#     "IFJCi4AUkSYqIQkQSoghodkVUcERRUUEG8igiAOOjoCMFVEsDIoK2AfkIaKOg6OIisr74Xuj"
#     "a9a89+bN/rXXPues852zzwfACAyWSDNRNYAMqUIeEeCDx8TG4eQuQIEKJHAAEAizZCFz/SMB"
#     "APh+PDwrIsAHvgABeNMLCADATZvAMByH/w/qQplcAYCEAcB0kThLCIAUAEB6jkKmAEBGAYCd"
#     "mCZTAKAEAGDLY2LjAFAtAGAnf+bTAICd+Jl7AQBblCEVAaCRACATZYhEAGg7AKzPVopFAFgw"
#     "ABRmS8Q5ANgtADBJV2ZIALC3AMDOEAuyAAgMADBRiIUpAAR7AGDIIyN4AISZABRG8lc88Suu"
#     "EOcqAAB4mbI8uSQ5RYFbCC1xB1dXLh4ozkkXKxQ2YQJhmkAuwnmZGTKBNA/g88wAAKCRFRHg"
#     "g/P9eM4Ors7ONo62Dl8t6r8G/yJiYuP+5c+rcEAAAOF0ftH+LC+zGoA7BoBt/qIl7gRoXgug"
#     "dfeLZrIPQLUAoOnaV/Nw+H48PEWhkLnZ2eXk5NhKxEJbYcpXff5nwl/AV/1s+X48/Pf14L7i"
#     "JIEyXYFHBPjgwsz0TKUcz5IJhGLc5o9H/LcL//wd0yLESWK5WCoU41EScY5EmozzMqUiiUKS"
#     "KcUl0v9k4t8s+wM+3zUAsGo+AXuRLahdYwP2SycQWHTA4vcAAPK7b8HUKAgDgGiD4c93/+8/"
#     "/UegJQCAZkmScQAAXkQkLlTKsz/HCAAARKCBKrBBG/TBGCzABhzBBdzBC/xgNoRCJMTCQhBC"
#     "CmSAHHJgKayCQiiGzbAdKmAv1EAdNMBRaIaTcA4uwlW4Dj1wD/phCJ7BKLyBCQRByAgTYSHa"
#     "iAFiilgjjggXmYX4IcFIBBKLJCDJiBRRIkuRNUgxUopUIFVIHfI9cgI5h1xGupE7yAAygvyG"
#     "vEcxlIGyUT3UDLVDuag3GoRGogvQZHQxmo8WoJvQcrQaPYw2oefQq2gP2o8+Q8cwwOgYBzPE"
#     "bDAuxsNCsTgsCZNjy7EirAyrxhqwVqwDu4n1Y8+xdwQSgUXACTYEd0IgYR5BSFhMWE7YSKgg"
#     "HCQ0EdoJNwkDhFHCJyKTqEu0JroR+cQYYjIxh1hILCPWEo8TLxB7iEPENyQSiUMyJ7mQAkmx"
#     "pFTSEtJG0m5SI+ksqZs0SBojk8naZGuyBzmULCAryIXkneTD5DPkG+Qh8lsKnWJAcaT4U+Io"
#     "UspqShnlEOU05QZlmDJBVaOaUt2ooVQRNY9aQq2htlKvUYeoEzR1mjnNgxZJS6WtopXTGmgX"
#     "aPdpr+h0uhHdlR5Ol9BX0svpR+iX6AP0dwwNhhWDx4hnKBmbGAcYZxl3GK+YTKYZ04sZx1Qw"
#     "NzHrmOeZD5lvVVgqtip8FZHKCpVKlSaVGyovVKmqpqreqgtV81XLVI+pXlN9rkZVM1PjqQnU"
#     "lqtVqp1Q61MbU2epO6iHqmeob1Q/pH5Z/YkGWcNMw09DpFGgsV/jvMYgC2MZs3gsIWsNq4Z1"
#     "gTXEJrHN2Xx2KruY/R27iz2qqaE5QzNKM1ezUvOUZj8H45hx+Jx0TgnnKKeX836K3hTvKeIp"
#     "G6Y0TLkxZVxrqpaXllirSKtRq0frvTau7aedpr1Fu1n7gQ5Bx0onXCdHZ4/OBZ3nU9lT3acK"
#     "pxZNPTr1ri6qa6UbobtEd79up+6Ynr5egJ5Mb6feeb3n+hx9L/1U/W36p/VHDFgGswwkBtsM"
#     "zhg8xTVxbzwdL8fb8VFDXcNAQ6VhlWGX4YSRudE8o9VGjUYPjGnGXOMk423GbcajJgYmISZL"
#     "TepN7ppSTbmmKaY7TDtMx83MzaLN1pk1mz0x1zLnm+eb15vft2BaeFostqi2uGVJsuRaplnu"
#     "trxuhVo5WaVYVVpds0atna0l1rutu6cRp7lOk06rntZnw7Dxtsm2qbcZsOXYBtuutm22fWFn"
#     "Yhdnt8Wuw+6TvZN9un2N/T0HDYfZDqsdWh1+c7RyFDpWOt6azpzuP33F9JbpL2dYzxDP2DPj"
#     "thPLKcRpnVOb00dnF2e5c4PziIuJS4LLLpc+Lpsbxt3IveRKdPVxXeF60vWdm7Obwu2o26/u"
#     "Nu5p7ofcn8w0nymeWTNz0MPIQ+BR5dE/C5+VMGvfrH5PQ0+BZ7XnIy9jL5FXrdewt6V3qvdh"
#     "7xc+9j5yn+M+4zw33jLeWV/MN8C3yLfLT8Nvnl+F30N/I/9k/3r/0QCngCUBZwOJgUGBWwL7"
#     "+Hp8Ib+OPzrbZfay2e1BjKC5QRVBj4KtguXBrSFoyOyQrSH355jOkc5pDoVQfujW0Adh5mGL"
#     "w34MJ4WHhVeGP45wiFga0TGXNXfR3ENz30T6RJZE3ptnMU85ry1KNSo+qi5qPNo3ujS6P8Yu"
#     "ZlnM1VidWElsSxw5LiquNm5svt/87fOH4p3iC+N7F5gvyF1weaHOwvSFpxapLhIsOpZATIhO"
#     "OJTwQRAqqBaMJfITdyWOCnnCHcJnIi/RNtGI2ENcKh5O8kgqTXqS7JG8NXkkxTOlLOW5hCep"
#     "kLxMDUzdmzqeFpp2IG0yPTq9MYOSkZBxQqohTZO2Z+pn5mZ2y6xlhbL+xW6Lty8elQfJa7OQ"
#     "rAVZLQq2QqboVFoo1yoHsmdlV2a/zYnKOZarnivN7cyzytuQN5zvn//tEsIS4ZK2pYZLVy0d"
#     "WOa9rGo5sjxxedsK4xUFK4ZWBqw8uIq2Km3VT6vtV5eufr0mek1rgV7ByoLBtQFr6wtVCuWF"
#     "fevc1+1dT1gvWd+1YfqGnRs+FYmKrhTbF5cVf9go3HjlG4dvyr+Z3JS0qavEuWTPZtJm6ebe"
#     "LZ5bDpaql+aXDm4N2dq0Dd9WtO319kXbL5fNKNu7g7ZDuaO/PLi8ZafJzs07P1SkVPRU+lQ2"
#     "7tLdtWHX+G7R7ht7vPY07NXbW7z3/T7JvttVAVVN1WbVZftJ+7P3P66Jqun4lvttXa1ObXHt"
#     "xwPSA/0HIw6217nU1R3SPVRSj9Yr60cOxx++/p3vdy0NNg1VjZzG4iNwRHnk6fcJ3/ceDTra"
#     "dox7rOEH0x92HWcdL2pCmvKaRptTmvtbYlu6T8w+0dbq3nr8R9sfD5w0PFl5SvNUyWna6YLT"
#     "k2fyz4ydlZ19fi753GDborZ752PO32oPb++6EHTh0kX/i+c7vDvOXPK4dPKy2+UTV7hXmq86"
#     "X23qdOo8/pPTT8e7nLuarrlca7nuer21e2b36RueN87d9L158Rb/1tWeOT3dvfN6b/fF9/Xf"
#     "Ft1+cif9zsu72Xcn7q28T7xf9EDtQdlD3YfVP1v+3Njv3H9qwHeg89HcR/cGhYPP/pH1jw9D"
#     "BY+Zj8uGDYbrnjg+OTniP3L96fynQ89kzyaeF/6i/suuFxYvfvjV69fO0ZjRoZfyl5O/bXyl"
#     "/erA6xmv28bCxh6+yXgzMV70VvvtwXfcdx3vo98PT+R8IH8o/2j5sfVT0Kf7kxmTk/8EA5jz"
#     "/GMzLdsAAAAEZ0FNQQAAsY58+1GTAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAA"
#     "ADqYAAAXb5JfxUYAAAMAUExURfjeBFZNBv+0AGtjWdkAALwAAGoDA/g4OP///wAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKoNeNYAAAAJdFJOU///////////AFNP"
#     "eBIAAABSSURBVHjafIwxDoAwDMR8KSj8/7cduDIUAenAFMU6WwcA9JyXuP/RKyDUC8jBvXkU"
#     "FgUri6KWZeEduyhuqg15jfIPvAAP0DnBBhBGKF7wLV0DABGRFSaXe5wjAAAAAElFTkSuQmCC")
# IconManager._catalog['dimlayersofficon'] = dimlayersofficon

# #----------------------------------------------------------------------
# dimlayersonicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAACXBIWXMAAAsTAAALEwEAmpwY"
#     "AAAKT2lDQ1BQaG90b3Nob3AgSUNDIHByb2ZpbGUAAHjanVNnVFPpFj333vRCS4iAlEtvUhUI"
#     "IFJCi4AUkSYqIQkQSoghodkVUcERRUUEG8igiAOOjoCMFVEsDIoK2AfkIaKOg6OIisr74Xuj"
#     "a9a89+bN/rXXPues852zzwfACAyWSDNRNYAMqUIeEeCDx8TG4eQuQIEKJHAAEAizZCFz/SMB"
#     "APh+PDwrIsAHvgABeNMLCADATZvAMByH/w/qQplcAYCEAcB0kThLCIAUAEB6jkKmAEBGAYCd"
#     "mCZTAKAEAGDLY2LjAFAtAGAnf+bTAICd+Jl7AQBblCEVAaCRACATZYhEAGg7AKzPVopFAFgw"
#     "ABRmS8Q5ANgtADBJV2ZIALC3AMDOEAuyAAgMADBRiIUpAAR7AGDIIyN4AISZABRG8lc88Suu"
#     "EOcqAAB4mbI8uSQ5RYFbCC1xB1dXLh4ozkkXKxQ2YQJhmkAuwnmZGTKBNA/g88wAAKCRFRHg"
#     "g/P9eM4Ors7ONo62Dl8t6r8G/yJiYuP+5c+rcEAAAOF0ftH+LC+zGoA7BoBt/qIl7gRoXgug"
#     "dfeLZrIPQLUAoOnaV/Nw+H48PEWhkLnZ2eXk5NhKxEJbYcpXff5nwl/AV/1s+X48/Pf14L7i"
#     "JIEyXYFHBPjgwsz0TKUcz5IJhGLc5o9H/LcL//wd0yLESWK5WCoU41EScY5EmozzMqUiiUKS"
#     "KcUl0v9k4t8s+wM+3zUAsGo+AXuRLahdYwP2SycQWHTA4vcAAPK7b8HUKAgDgGiD4c93/+8/"
#     "/UegJQCAZkmScQAAXkQkLlTKsz/HCAAARKCBKrBBG/TBGCzABhzBBdzBC/xgNoRCJMTCQhBC"
#     "CmSAHHJgKayCQiiGzbAdKmAv1EAdNMBRaIaTcA4uwlW4Dj1wD/phCJ7BKLyBCQRByAgTYSHa"
#     "iAFiilgjjggXmYX4IcFIBBKLJCDJiBRRIkuRNUgxUopUIFVIHfI9cgI5h1xGupE7yAAygvyG"
#     "vEcxlIGyUT3UDLVDuag3GoRGogvQZHQxmo8WoJvQcrQaPYw2oefQq2gP2o8+Q8cwwOgYBzPE"
#     "bDAuxsNCsTgsCZNjy7EirAyrxhqwVqwDu4n1Y8+xdwQSgUXACTYEd0IgYR5BSFhMWE7YSKgg"
#     "HCQ0EdoJNwkDhFHCJyKTqEu0JroR+cQYYjIxh1hILCPWEo8TLxB7iEPENyQSiUMyJ7mQAkmx"
#     "pFTSEtJG0m5SI+ksqZs0SBojk8naZGuyBzmULCAryIXkneTD5DPkG+Qh8lsKnWJAcaT4U+Io"
#     "UspqShnlEOU05QZlmDJBVaOaUt2ooVQRNY9aQq2htlKvUYeoEzR1mjnNgxZJS6WtopXTGmgX"
#     "aPdpr+h0uhHdlR5Ol9BX0svpR+iX6AP0dwwNhhWDx4hnKBmbGAcYZxl3GK+YTKYZ04sZx1Qw"
#     "NzHrmOeZD5lvVVgqtip8FZHKCpVKlSaVGyovVKmqpqreqgtV81XLVI+pXlN9rkZVM1PjqQnU"
#     "lqtVqp1Q61MbU2epO6iHqmeob1Q/pH5Z/YkGWcNMw09DpFGgsV/jvMYgC2MZs3gsIWsNq4Z1"
#     "gTXEJrHN2Xx2KruY/R27iz2qqaE5QzNKM1ezUvOUZj8H45hx+Jx0TgnnKKeX836K3hTvKeIp"
#     "G6Y0TLkxZVxrqpaXllirSKtRq0frvTau7aedpr1Fu1n7gQ5Bx0onXCdHZ4/OBZ3nU9lT3acK"
#     "pxZNPTr1ri6qa6UbobtEd79up+6Ynr5egJ5Mb6feeb3n+hx9L/1U/W36p/VHDFgGswwkBtsM"
#     "zhg8xTVxbzwdL8fb8VFDXcNAQ6VhlWGX4YSRudE8o9VGjUYPjGnGXOMk423GbcajJgYmISZL"
#     "TepN7ppSTbmmKaY7TDtMx83MzaLN1pk1mz0x1zLnm+eb15vft2BaeFostqi2uGVJsuRaplnu"
#     "trxuhVo5WaVYVVpds0atna0l1rutu6cRp7lOk06rntZnw7Dxtsm2qbcZsOXYBtuutm22fWFn"
#     "Yhdnt8Wuw+6TvZN9un2N/T0HDYfZDqsdWh1+c7RyFDpWOt6azpzuP33F9JbpL2dYzxDP2DPj"
#     "thPLKcRpnVOb00dnF2e5c4PziIuJS4LLLpc+Lpsbxt3IveRKdPVxXeF60vWdm7Obwu2o26/u"
#     "Nu5p7ofcn8w0nymeWTNz0MPIQ+BR5dE/C5+VMGvfrH5PQ0+BZ7XnIy9jL5FXrdewt6V3qvdh"
#     "7xc+9j5yn+M+4zw33jLeWV/MN8C3yLfLT8Nvnl+F30N/I/9k/3r/0QCngCUBZwOJgUGBWwL7"
#     "+Hp8Ib+OPzrbZfay2e1BjKC5QRVBj4KtguXBrSFoyOyQrSH355jOkc5pDoVQfujW0Adh5mGL"
#     "w34MJ4WHhVeGP45wiFga0TGXNXfR3ENz30T6RJZE3ptnMU85ry1KNSo+qi5qPNo3ujS6P8Yu"
#     "ZlnM1VidWElsSxw5LiquNm5svt/87fOH4p3iC+N7F5gvyF1weaHOwvSFpxapLhIsOpZATIhO"
#     "OJTwQRAqqBaMJfITdyWOCnnCHcJnIi/RNtGI2ENcKh5O8kgqTXqS7JG8NXkkxTOlLOW5hCep"
#     "kLxMDUzdmzqeFpp2IG0yPTq9MYOSkZBxQqohTZO2Z+pn5mZ2y6xlhbL+xW6Lty8elQfJa7OQ"
#     "rAVZLQq2QqboVFoo1yoHsmdlV2a/zYnKOZarnivN7cyzytuQN5zvn//tEsIS4ZK2pYZLVy0d"
#     "WOa9rGo5sjxxedsK4xUFK4ZWBqw8uIq2Km3VT6vtV5eufr0mek1rgV7ByoLBtQFr6wtVCuWF"
#     "fevc1+1dT1gvWd+1YfqGnRs+FYmKrhTbF5cVf9go3HjlG4dvyr+Z3JS0qavEuWTPZtJm6ebe"
#     "LZ5bDpaql+aXDm4N2dq0Dd9WtO319kXbL5fNKNu7g7ZDuaO/PLi8ZafJzs07P1SkVPRU+lQ2"
#     "7tLdtWHX+G7R7ht7vPY07NXbW7z3/T7JvttVAVVN1WbVZftJ+7P3P66Jqun4lvttXa1ObXHt"
#     "xwPSA/0HIw6217nU1R3SPVRSj9Yr60cOxx++/p3vdy0NNg1VjZzG4iNwRHnk6fcJ3/ceDTra"
#     "dox7rOEH0x92HWcdL2pCmvKaRptTmvtbYlu6T8w+0dbq3nr8R9sfD5w0PFl5SvNUyWna6YLT"
#     "k2fyz4ydlZ19fi753GDborZ752PO32oPb++6EHTh0kX/i+c7vDvOXPK4dPKy2+UTV7hXmq86"
#     "X23qdOo8/pPTT8e7nLuarrlca7nuer21e2b36RueN87d9L158Rb/1tWeOT3dvfN6b/fF9/Xf"
#     "Ft1+cif9zsu72Xcn7q28T7xf9EDtQdlD3YfVP1v+3Njv3H9qwHeg89HcR/cGhYPP/pH1jw9D"
#     "BY+Zj8uGDYbrnjg+OTniP3L96fynQ89kzyaeF/6i/suuFxYvfvjV69fO0ZjRoZfyl5O/bXyl"
#     "/erA6xmv28bCxh6+yXgzMV70VvvtwXfcdx3vo98PT+R8IH8o/2j5sfVT0Kf7kxmTk/8EA5jz"
#     "/GMzLdsAAAAEZ0FNQQAAsY58+1GTAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAA"
#     "ADqYAAAXb5JfxUYAAAMAUExURWtjWdkAALwAAGoDA/g4OCsoKP///wAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEdAJXUAAAAHdFJOU////////wAaSwNG"
#     "AAAAS0lEQVR42oTOwQrAMAgD0KQZ+///Hak7dKPWHuol8Igib6zTRkQFRoHZ+YFbY4Pny2uE"
#     "AUO50cVytB+PruACDoBOIIJsSn9orrwDADg4DCecjgTqAAAAAElFTkSuQmCC")
# IconManager._catalog['dimlayersonicon'] = dimlayersonicon

# #----------------------------------------------------------------------
# enemiesicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAAd0SU1FB9sKFgUCFkvGQ5YAAAAZ"
#     "dEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAAAvUlEQVQ4y62TzQ3CMAyFX3Ii"
#     "Rw7eoD12CTZIZkDdoRMwQ6TOkBEYoj12hB440ps5oEj9wcgtWLJkJfYXJy8GM8MXnuuqZmaG"
#     "xuf5xheeyRFiFw12WCgDk6M3AADWkFAGzrG0twAcMXIEm4ZkjhbHLhoLAHsh8yvZvKiFrN/D"
#     "4kdbANKQDDlCO/WbU9upxye5xQ4yhBzh9rjrOgCA8TmiOV82iddTpQNkSC6YxyqApIb03f+r"
#     "gtTF12HTjq3kLw9omovanQFqAAAAAElFTkSuQmCC")
# IconManager._catalog['enemiesicon'] = enemiesicon

# #----------------------------------------------------------------------
# eventlayericon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAAd0SU1FB9sKFgQ5AfVlQ14AAAAZ"
#     "dEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAABEklEQVQ4y6WTMU7DQBBF3yIL"
#     "FEXZwrLcQJkCkxq5TcENqEmZO3AVyqTODShordQRd1iFFIssiwhpKDY26zibRPCl0Vr2/j8z"
#     "f8bgIPwRUYC8/06FBC4ApuNRTRJApNCIpYljFUZNykJD5m5v7lIgxZQVy+8vYB0SUY3A5tGR"
#     "QvATACj924J6eVvxPLxqPpqy6gjMHy6ZXyfwrmuyarXgI+33MGVF2u9xX8JskDD5XCOWFrkx"
#     "MSTSaVh3J3Kwgtq8p9ctMXALTHLng8qt+CItgXhh3Lkjqdy2lTMbNnk6Hom/C3V83AxFrHue"
#     "DRKRQos/0ujExkm8MCi9GyNbyKxv5sEq9lc6FGETz/kHTo7xXPxb4AeaEGg3jGjIlQAAAABJ"
#     "RU5ErkJggg==")
# IconManager._catalog['eventlayericon'] = eventlayericon

# #----------------------------------------------------------------------
# itemsicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAAd0SU1FB9sKFgQ7LmyCHIUAAAAZ"
#     "dEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAAAuklEQVQ4y2P8//8/AzbQySiG"
#     "IlH+/xUjNnVMDBQCRmwu8PT0/M/AwMCgy/CSgYGBgeEygzgDAwMDw/bt2xmJcgFMoYuRGoOL"
#     "kRpOzQwMDAwM////x4o9PDz+Y2OjY4rDAK8BDp5n/zMufvmfbAModgHZBnh6ev7/ztAC5++I"
#     "WgCPWoIGoGu2X/YEryFM+DQTYwgTIc2EDGEiRjMymGnOxBA4cRHcEKJj4WCUDJydpiaKmZlw"
#     "hTIuAMsbANmReTg7+5e0AAAAAElFTkSuQmCC")
# IconManager._catalog['itemsicon'] = itemsicon

# #----------------------------------------------------------------------
# newicon= PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9sKAhEfGnlIqMUAAAFa"
#     "SURBVDjLjZM/SAJRHMc/yq2JtwSFFurg4OAkUtPNJSQuLQUubUqbjd7aGLRFS7W4xAnp0OSk"
#     "4G3tWnGi4HKVu6/hPLk/Xt0XHrz3ffy+fN/v977ghlit0Ig4izvTJHU9z/jkBVX5v1jtEZGC"
#     "Li+ftPX+++2B+czAHKUBGPRbHByeotISUaftup5fF8mJMnKi7BO2i+XMGADJtu1Eul1yCYlm"
#     "ln3g1eYyY7Z3koCOFKZRn8Uc85kBI+vcfdQBHbVn9dB+guhMkyLdLgknZ040YU408dGtiOF9"
#     "QaiKe0qSYxKuC9HMWpu7KwDiAMUcoOMV2Iivi2sft1zEgOdAgcjxriHAwJxovmJzESP6fuvj"
#     "XQ5UxZp/fGXbiTig78WCBezm3JyVA6dxdF7YLKAqiGqjwjJVQ976Wdu1f9+g36LaqFij9CAa"
#     "NjTLVO3vMIVxYQcoKI14P8mm9Hm5XwRikENN5AXIAAAAAElFTkSuQmCC")
# IconManager._catalog['newicon'] = newicon

# #----------------------------------------------------------------------
# openicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9sKAhEgIOeaW0sAAADG"
#     "SURBVDjLY2DADf4zEAGYcGpe9IIoQxhxabZf9oSBgYGB4eAOE1zqsBqAohkG8BnCSEgzIUMY"
#     "sQYcphdwuoAFi4EYAdfggD1WGg4wMLIQE1X5SzYwvP/Mx8B0fwrDq+ePGd7fVWI4fmwlZjQ2"
#     "OGCPNmyaLa3CGRocGP5juODBtiAGBS8JhoMwzU82MLz/TEQ6wGU7PtBwgIGREaY5oSyI4Z9i"
#     "DoMg7ye8TkfWzMDAwMBEimZLq3AUzfjyAtGAkVT/I9tOFQAAXcVrgpXQPZMAAAAASUVORK5C"
#     "YII=")
# IconManager._catalog['openicon'] = openicon


# #----------------------------------------------------------------------
# pasteicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAAd0SU1FB9sKFgQ1JWXT6IMAAAAZ"
#     "dEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAABSUlEQVQ4y42TsUvDUBCHv0D+"
#     "gE7BqUMHdxfp4iIZnBzaQTroIi4tuJbaoR1aJeBUsIubizroUgoVgouLKOJiIR0KdnEQCqEg"
#     "FCqcg7yal8S0Bw/e/Y773r279xARwqtWq0mcHrcMEUFZvV4XANu2cV1XaQYJZgI4hvWb+HAL"
#     "gOu62LZNMFaWz1iQ6RiWrB1taqJKBlAxx7AkDmKqzXqxAIyjRxQLPLUvk6/wn50dnvw5uQzN"
#     "fFaC8erNo2EmJZdaFQCmkz5fH6sA+KMBvW6H/cY2zXxWEisASJ2XNf8lvQswBy4E+AeODvRm"
#     "QAd/NFgMmE76rFxf6NrOHgC9bie5B6rMYAXTSV9r4FJXCPdguNGIH2Nw1s/eOwBX7VMgpSVs"
#     "pQdRwOvx/Vz4zmUi41OjK7UqDO/edED4eYYfS9DG3iyiab9xGUiwgQA/hoWvgy6a+sIAAAAA"
#     "SUVORK5CYII=")
# IconManager._catalog['pasteicon'] = pasteicon

# #----------------------------------------------------------------------
# redoicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9sKAhE6EQZpoaoAAACg"
#     "SURBVDjLY2AYaMCILtDBIPqfGI0VDK8ZMQzoYBD9nyrDT1Cz0KSlDIxB5owMDAwMTKRqRgcs"
#     "+GwhGnQwiP5/K6MCx8SGA4oXSLGMIgPQDYHHwv91J/+/y4uGK5r95CNOA1Jl+BlmP/nIUMHw"
#     "mpEFnyJ8IFWGn4HhCcN/lHSA7gqi0gO64P91JwnGwLu8aJTERBL4v+7kf2IswWsAVXMjAN3N"
#     "PlQtOFuBAAAAAElFTkSuQmCC")
# IconManager._catalog['redoicon'] = redoicon


# #----------------------------------------------------------------------
# saveicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9sKAhEhJhfizz8AAAFk"
#     "SURBVDjLlVOxSsNQFD2vdHCpkKGCYAfjBzgptBLIBxQaOtilguCq4CQZ3xjcBFdBcOpSLLSO"
#     "JXCpQvsBnRodpEuHQF06eR2Sl6RpqvVA4D5ezrn3nnufQAxOxAIbIqfIvWkJeqcKvVNNi2WB"
#     "1ZfDP7CwwUTECxtY2HEFDABXo8OsLBGIKLOqfG9aWiGHbcCrdTn0IyIPjDpAFBwcQwjVf1rE"
#     "q3WVmUwhYWDUcW3Pon+2HAiRNFGJrCOfUBsAYBhGPClpgqUZOKp3qgzEZyJiImIHxShOe5MH"
#     "gHKlgeGZh+NaF964D60wh9yzfs+s9kC6EG+vLfgTHcOHI+Te7+F/bWeSpZkxhXUzd1CEjRkQ"
#     "ZIX/+RxcNC2WblxFFEgTXK40oB146F984HTcglaYZ4rfNS0okaV+kiIvT6M/N1O6EGtbOL+p"
#     "4/G2DSW4s1vC9/7lclVNa/ktJA3dFCvPNtyBjSBdiB/31J/v3iOXWgAAAABJRU5ErkJggg==")
# IconManager._catalog['saveicon'] = saveicon

# #----------------------------------------------------------------------
# skillsicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAAd0SU1FB9sKFgQ7ClCB+FQAAAAZ"
#     "dEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAABCElEQVQ4y2NgoBAwEqOIV8Dw"
#     "P4z9+cN5RpJs4BUw/G/vceY/w6IX/2fefPUf2TCSNcPYyIYwkeKacydSGeyXPWH4PGk73FtM"
#     "+Gw3spjNcDBKhmGmOROKIch8JlI0wwKxxNwd7gpGXAZ8yv8G58+KOgxnl5i7M3z+cJ4R5gUW"
#     "XF7gm8gFZ39isEUYwMAFdwlGjPAKGP6HYfSog+H/9eooscCInFBw+ZuBgYEh/eQ/Bt48Twb0"
#     "BMWIHmA9IYsZGBgYGL5+uszAwMDAwM2ny/D102WG+l1dGAZ9/nCeEa8LGt3K4DZy8+lCwmBN"
#     "LFYXoYQBsv+RMcOiF/+l5BNQUiMjocyDC5CcqXABABnvpUckWmVZAAAAAElFTkSuQmCC")
# IconManager._catalog['skillsicon'] = skillsicon

# #----------------------------------------------------------------------
# statesicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAAd0SU1FB9sKFgUDHLIIm8kAAAAZ"
#     "dEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAAAe0lEQVQ4y2P8//8/AyWAiYFC"
#     "QEMDGjQQfjvF/x+O0QAj1jBA1txwgxFFDmaI2UeI+P///xH4JN9/OLte/T+KHDqGqsWumQRM"
#     "nmYk15EeC7DwgdGUugCvJF7NUBo1GpGjD1sUYgGY6QDuR6hm9MQDi38YIOREQphxwHMjACnN"
#     "Q90G3qnXAAAAAElFTkSuQmCC")
# IconManager._catalog['statesicon'] = statesicon

# #----------------------------------------------------------------------
# systemicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAAd0SU1FB9sKFgUHGj8H+/gAAAAZ"
#     "dEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAAAs0lEQVQ4y6VSQREEIQwLzJmp"
#     "DzygACHoQAEe+kPEymFfZXpsy9zc5sVQkqahYc6JN4inIhFNIpo/C2gCEc3WGnLO0He7YNTk"
#     "nbCLW/XHCCkl5JwfVltr5ghBhyhdPDAzeu+4riuYIwBAKcUV6L1/vV0OrM7MjForAGCM4TqJ"
#     "eImVgbbl5aDHkxzifnEKUX7HDVHIzLy66bN88XEPJKCTfY2PHkGU9dmrm4tkre9OOG7iP7gB"
#     "N9SEJ9MU9N4AAAAASUVORK5CYII=")
# IconManager._catalog['systemicon'] = systemicon

# #----------------------------------------------------------------------
# tilesetsicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAAd0SU1FB9sKFgUGDjzGHsQAAAAZ"
#     "dEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAABCUlEQVQ4y3VSsa3FIAy8RCnf"
#     "DlSRwgyv9Q6eICtkiKzABOyQ9s1A4YodXvkk/wq+gcRSJOfwmfMZqCpUFdu2acktdofbb4YJ"
#     "773a/PP94fP9NXgfk6rWYgB4v5anWqSUph6bLRkAbM7MOI5jIFtFS0ppepJIRNj3HU9jAvj3"
#     "gJnBzI9Sn3ypDWKMcM41BBFBCKG5+f1aqk/ee222sK4r+n8RaVT1vtQGIQRc1zXIzjkP2Hme"
#     "owciAiIaRugxIqoKmgZ3TtvbCyYizaiTqtaCMoZzrhYVQvEi54wYY/Vk7iXHGAdyMdTOXh/S"
#     "07MVkUpg5upFv+phjWXvNgrp7qxRUNZIRMObsGc2/gCXrMEO4F1GMgAAAABJRU5ErkJggg==")
# IconManager._catalog['tilesetsicon'] = tilesetsicon

# #----------------------------------------------------------------------
# troopsicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAAd0SU1FB9sKFgUCNwevU8gAAAAZ"
#     "dEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAABYElEQVQ4y6WTL2/CUBTFf4+A"
#     "QC3L0mQCxUAggKAwiOIxr35y7cdgnwBfZkjmqSFBblkwE8tCNZuaq1hWM3kn+h9azF5yk3d6"
#     "37s959z7lIjwn1UDcAaOWF2rtJLVtcQZONV/sfu26I4WEaEqdEeL3bdLz9TzxZyBI8FvkGKj"
#     "aeD6rjonoZ6nepwMfgOqpKUeuL6rjKZx1qhzTGp5sD54JMWMpsH64AGwvFqipqqcSWKG3bdF"
#     "QAQiU0Ew47iPI8aVJlodne6VCZjRvj2aAfDJJspNlciTqIKJru+q4y6kF983Rfy8Oe1Cfnkt"
#     "D0z4uH4B4Ca+mGBlZiwKJuY70h7NUNsQemF2oBeitmHK5KQLieN57WqR5dQik0HMolYmoT2a"
#     "pbr1XjNcNRiuGui9Tj1JCtWrhmcuc/yVz9jbcde6AODh6weYcDuY88hbxOr4OScDoy81Y2/H"
#     "q54U8sk37zsasj8faL/j8ivJRAAAAABJRU5ErkJggg==")
# IconManager._catalog['troopsicon'] = troopsicon

# #----------------------------------------------------------------------
# Undo_Redo = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAAEAAAAAQCAYAAACm53kpAAABAUlEQVR4nOWWMQ6DMAxFfQm2"
#     "dkE9DgfjNJEYegKmXKRbFy7gDm2qEMeOgRCr6vAlpIi8Z5PIwDzP8M8xF7DO9wEXQFwA+2kQ"
#     "U9pwhA6loPOIzpN9Stxa/JDsCQhNCLk/riSSxAgdPi83klA0V3xg53g1+Dkf1RXgmpGTSOGl"
#     "gvc2QMuv0gBOsCSgLVo6fdJp3PoBctncgH4aWIkUHt+xWjmLTyBnC0hrFvwVoJVAbt2Kv9pc"
#     "Gj8xHBcgAHSeSHBJJS35pLOaaAQ0GaEjxbXmbxo/HHyvBDrP/m+04r9f/EiURpEEjyVKSUel"
#     "JR9iCQ3gaLifIys+kWghwK4Z8E+F/UJeW7919GIJh+wAAAAASUVORK5CYII=")
# IconManager._catalog['Undo-Redo'] = Undo_Redo

# #----------------------------------------------------------------------
# undoicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9sKAhE5MRYq0qEAAACV"
#     "SURBVDjLY2AYaMAIYyht9PlPjIZ7/lsYsRrw/xPD/21fZAkakHtaH8UQJlKdPNn0IoprWZAl"
#     "vXge49SIy3VwFzDyMTDiw7mn9bG6AsULxAYkVheQoxkeC0obff5PNr3IgOxMbIGHHFaMfBC9"
#     "jDDNpAAUA4iNf2ya4V6AGYIvGpFjC6vE/08M//9/YvhPUcag2AByAACaWT50qqt4BwAAAABJ"
#     "RU5ErkJggg==")
# IconManager._catalog['undoicon'] = undoicon

# #----------------------------------------------------------------------
# weaponsicon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAAZiS0dE"
#     "AP8A/wD/oL2nkwAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAAd0SU1FB9sKFgUAGwdBXakAAAAZ"
#     "dEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAABAUlEQVQ4y6WSP2vCUBTFT6MF"
#     "QUmbILqUTIVm7pbl7XZzcMik+12UDP0cfoRCNimO3f0UoWOmFixI0KnB46B5+Acbn73j4/3u"
#     "veecC/yzbq5guM9bprCIgORV21JESJJpmrLYpGIyOQgCOI4Dz/OM5FNEGMfxweQyc8zh8bB1"
#     "/EHDSZKcha0djPQ7x3jYKjbRmpVS8H3/rObikVHoAgC8dhWfvz0NmxjGKHT5NXrlz8MjuQ27"
#     "NPCTQ7qdvAMABi93RqfMfsdG876K+SJHtlrDrlvIVmtMZ8s/JViF/uenGuaLHG8fGaazpW7S"
#     "VQ2USWG/YzMK3ZMYu6pxkQ86uguP66A2FaOCgASZAZIAAAAASUVORK5CYII=")
# IconManager._catalog['weaponsicon'] = weaponsicon

# #----------------------------------------------------------------------
# cuticon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAtklEQVR4nJ2SwQ3DIAxF/yA5"
#     "5uhF2CYbeIfcei3MkT26QVUpM7iXGNkGVJqDhZB4zx8Dciqwte2HbPshuiciISKJ57R+wuey"
#     "yrmsQ4nfPN9VoLAmGElc954gpwIA84LH6+MEFgYgcSbd+L37Kxxn0o1fpRdk4TiTbnxNAMDB"
#     "AJoB1/gqUCiWRm+uYLsDEGYWZnbd7YdqhmgFFtZ19AMbQYSnBb3Os/D1UrgNV8Fd2Am0/oFz"
#     "KvgCzbu/HzwNSBEAAAAASUVORK5CYII=")
# IconManager._catalog['cuticon'] = cuticon

# #----------------------------------------------------------------------
# check_empty = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAAA4AAAAMCAYAAABSgIzaAAAABGdBTUEAALGPC/xhBQAAAAlw"
#     "SFlzAAAOwgAADsIBFShKgAAAABp0RVh0U29mdHdhcmUAUGFpbnQuTkVUIHYzLjUuMTAw9HKh"
#     "AAAAKklEQVQoU2M4cODAf1Lw////GUCYAaTpz58/RGGQ2lGNOAJrRAYOOUkOAChoYZeQ/clq"
#     "AAAAAElFTkSuQmCC")
# IconManager._catalog['check_empty'] = check_empty

# #----------------------------------------------------------------------
# check_plus = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAAA4AAAAMCAYAAABSgIzaAAAABGdBTUEAALGPC/xhBQAAAAlw"
#     "SFlzAAAOwgAADsIBFShKgAAAABp0RVh0U29mdHdhcmUAUGFpbnQuTkVUIHYzLjUuMTAw9HKh"
#     "AAAAbElEQVQoU83SwQ2AIAwFUEZhe9foUCIihZJv0oSAInry0HDhteUHQ0TypkTEoAwQM08V"
#     "7g7hYq2g2oY/gbre3en9dobYvfEJhrBfwzoIbeLcKpgEFOMxD2uUEs9DnQSUcx7Ddj1FSKUL"
#     "58uXK/39J5g8lhAaAAAAAElFTkSuQmCC")
# IconManager._catalog['check_plus'] = check_plus

# #----------------------------------------------------------------------
# check_minus = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAAA4AAAAMCAYAAABSgIzaAAAABGdBTUEAALGPC/xhBQAAAAlw"
#     "SFlzAAAOwgAADsIBFShKgAAAABp0RVh0U29mdHdhcmUAUGFpbnQuTkVUIHYzLjUuMTAw9HKh"
#     "AAAAXklEQVQoU2M4cODAf1Lw////GUCYAaTpz58/RGGQ2qGsUcFh+X98+Pv3b+BAxPAjIY0/"
#     "f/7ArhFXyIJsAmn6/fsX8RqRNf39+4c4jeia/v37R1gjNk2gUMEIHHKSHAACM0JQInLrmgAA"
#     "AABJRU5ErkJggg==")
# IconManager._catalog['check_minus'] = check_minus

# #----------------------------------------------------------------------
# play_button = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1B"
#     "AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAadEVYdFNvZnR3YXJlAFBhaW50Lk5F"
#     "VCB2My41LjEwMPRyoQAAAXhJREFUOE/Nkb9LAnEYxs9LRfL0NH+kWCekZ2rS5VKEkiFKIYZW"
#     "WoY6RBhR0NRWS1ERRmVLDUVqmZEhBU6OQdDWvxEtQX/B01lLBKJCQ+/2wvt5ng/fL0H8q9HM"
#     "6p70C4Z3QkKmeDFBy3LsNgvPswvcaT+kdlmVD2BaCrFsWOCtuuCruOEtudAdZT4IcQs21jUL"
#     "/GU3xm9HESj6MVEIYnhzBBSrbM7GvmpF4NqP4FUQofw0prJziGaTmLyIwRSxNrZxrAwglPsG"
#     "I9kEZi4TiBXjiJfiSJYT8B74QNLC/brvwi0NfYFjZ0Fwx04Y00Zo99RQHynRldOhL+MASQnv"
#     "6gb0LjrQkzaB3pJDvkOBPpSCPpei44ZGe1QGQigo8LCybgAV58FdHsxIochSUD3I0Xmihtgs"
#     "eeWhcMMvpVIyKPIUNBUatkcG+nktBCKy1qpqCNcOVOtKDL6Y4bnnILfJmmv9mcyEdW/OZRak"
#     "qK351l9qBn7nmtL9q6NPOwWIjQURzaEAAAAASUVORK5CYII=")
# IconManager._catalog['play_button'] = play_button

# #----------------------------------------------------------------------
# pause_button = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1B"
#     "AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAadEVYdFNvZnR3YXJlAFBhaW50Lk5F"
#     "VCB2My41LjEwMPRyoQAAAhRJREFUOE/N099LU2EYB/DDhIocYYoQjGCbS7AgsB9grDGn+6XT"
#     "dIXhXT8u7cKG0fxxmkLpIrqL7mcejf6IOhcREdIPNxtZ5+TRprm5zkaenXl2ym+vEkfB410X"
#     "vfDAy/M+fHh4n/elqP9mXQpaRicZ78YE40Bs4gya3ZVJ0ty+sjLqxONHzjzDuPCEaQA9bFsn"
#     "+bZdjd+PnmWL6hX8LHVCLHoQHjCDFJnLD1JXC8VrkNTLyCt+fOLOb+ZHdgGj0eNsXmnFjzU3"
#     "0hk3boUsGpCT2yHKXqyKbsTfO/SBu/ds7GrOg+8pLxY++xC6sQ1kcgRNe/DtqxfTL536wMgd"
#     "G5ua92E+2QJuJoCbPTVaBynBA2HODz7eijcvmvSBodvHWD4RAPfhAkEuoq+3VgO4hI+g7eAT"
#     "nXj32q8PDPbVsnw8iMUvXUgvtyEcPqoBb58bMfPqAPhkNT7O1ukDdLiOXRI6sLJSg6xUgQG6"
#     "SgNmp8shcPuREY2YE0x73EHExGbESojrR7BWOgmatm7fQaoC2cJhMkYbhMWGPaYwVkXGaIVc"
#     "skMtdSEydEoDspKZoPVQ1ACWFrr1gbGolVXUFvxSrmOj0I/hwa0Hs/WQJNlF0G78lkNY5nv1"
#     "AVdj9bPJ8SY8jXVgKhaEw26SCHDIYKCaHz44janxADkLItJv3wR69P6gkSSdJBr/hmVHUf2O"
#     "/DmyN/yzT/wHUC0x8QGbNvUAAAAASUVORK5CYII=")
# IconManager._catalog['pause_button'] = pause_button

# #----------------------------------------------------------------------
# stop_button = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1B"
#     "AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAadEVYdFNvZnR3YXJlAFBhaW50Lk5F"
#     "VCB2My41LjEwMPRyoQAAAKFJREFUOE9jYKAGSGJg+N/KzEwSTgPqgdvdysT0/3t9/f/vjY3E"
#     "4aam/308PKgGvElI+P8mMZE4nJT0v5eTE8kARsb/D+3s/j+0tyca97CxIQxoAfrnmpzc/6tE"
#     "YpDabmCYwcMAZMAZYDiQgruQAxFsABCfJgEPRwMuA/1/iUgMUtuNkhKBnIck4h50Az4CBUjB"
#     "vcgGgDJGH4k4G9kASnI0ACf6d6zwpE1cAAAAAElFTkSuQmCC")
# IconManager._catalog['stop_button'] = stop_button

# #----------------------------------------------------------------------
# check_green = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAAA4AAAAMCAYAAABSgIzaAAAAAXNSR0IArs4c6QAAAARnQU1B"
#     "AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAadEVYdFNvZnR3YXJlAFBhaW50Lk5F"
#     "VCB2My41LjEwMPRyoQAAAFlJREFUKFO9kssJACAMQzuKq7tJBytUIgTEb/XgIbf3aAIVVfWb"
#     "uLsgAsnMQgH7R0w51UZXFyEdRQLcTCkkEuqlbdUWbiuywXbj7FJIBNRvDYurhxiqvrxcAcN6"
#     "Ngh8b3GxAAAAAElFTkSuQmCC")
# IconManager._catalog['check_green'] = check_green

# #----------------------------------------------------------------------
# map_icon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAALGOfPtRkwAAACBj"
#     "SFJNAAB6JQAAgIMAAPn/AACA6AAAdTAAAOpgAAA6lwAAF2+XqZnUAAAAwUlEQVR4nGL4//8/"
#     "AyUYIIAo0gzCAAEEJlqCzP+DMLGakNUDBBCY8/xaKxjDJAhhZPUAAQQ34P2TDSiSuDBIDUgt"
#     "jA0QQBgGnLm663/9xSX/65dcRGAgf+7tnXA1yAYABBCGATDFIAw3CERDMboBAAGEaQCSrTDD"
#     "YGLXb+3AMAAggLC6AN1WmCHYDAAIINwuAGJkb8DY6AYABBB2F6A5HW4QFgMAAojiaAQIIIoT"
#     "EkAAUZyUAQKI4swEEEAUGwAQYABRpNX0qsHD7gAAAABJRU5ErkJggg==")
# IconManager._catalog['map_icon'] = map_icon

# #----------------------------------------------------------------------
# project_icon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAALGOfPtRkwAAACBj"
#     "SFJNAAB6JQAAgIMAAPn/AACA6AAAdTAAAOpgAAA6lwAAF2+XqZnUAAAA5klEQVR4nGL4//8/"
#     "AyUYIIBQOEEMDP+Jwch6AAIIRfMlBYb/Dx3wY5AaZEMAAghD8xEG/BjdEIAAghsA07yWAIYZ"
#     "AjMAIIDgBnxIIGw7DIPUwgwACCC4AX/nM/z/V4/Al+QRGkBsZDmQWpgBAAGEMGA/KgYpfOgB"
#     "wWBNaPIwAwACCG7AbDS8HsnQ9VjkYQYABBBGLLwscIBH2b9+CIbxYXLIsQAQQBixgBxd2Njo"
#     "sQAQQBgGHHJwQIku5OgFyaEbABBAeNMBzEZ86QAggHC6ABvG5gKAACIpE2HLVAABRFFWBmGA"
#     "AAMAbGIf2XutwP8AAAAASUVORK5CYII=")
# IconManager._catalog['project_icon'] = project_icon 

# #----------------------------------------------------------------------
# script_icon = PyEmbeddedImage(
#     "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAALGOfPtRkwAAACBj"
#     "SFJNAAB6JQAAgIMAAPn/AACA6AAAdTAAAOpgAAA6lwAAF2+XqZnUAAAA5ElEQVR4nGL4//8/"
#     "Azn4MoPjfxANEEBgTkuQ+X9SMFgzgx+YBggguAHPr7UShc9vAWq5x/Af5gKAAIIZADfk/ZMN"
#     "ODFM857ZfP+TbTXBBgAEEIoLYAqv7J8ExshsdM0gS0F6AQIIqwH4bC4vigCrBekB6QUIIKxe"
#     "gNkKs3lHrwKGZpgLAAKIoAvWdUqAMUgziI9sOwgDBBDOMEB3CUwM3RCAAIInDGJiAVkzzAsA"
#     "AYQ3FtBdgs0FAAFEsgvQDQAIIKLTAYyPHogAAYThAmIxzBCAACIrM8EwSC9AAJGVlZExQIAB"
#     "ALAI4LT/xABjAAAAAElFTkSuQmCC")
# IconManager._catalog['script_icon'] = script_icon