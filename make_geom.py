def make_geom(shape):
    geom = shape["geometry"]
    t = geom["type"]
    points = []
    if t == "Polygon":
        multi = shapely.geometry.MultiPolygon([shapely.geometry.Polygon(geom["coordinates"][0])])
        return GEOSGeometry(multi.wkt)
    else:
        multi = shapely.geometry.MultiPolygon(map(lambda x: shapely.geometry.Polygon(x[0]), geom["coordinates"]))
        return GEOSGeometry(multi.wkt)
        
