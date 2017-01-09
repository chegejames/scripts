def make_file(county):
    county_name = re.sub("/", " ", county.name)+" COUNTY"
    county_geom = county.geom
    os.mkdir(county_name)
    os.chdir(county_name)
    Consts = county.constituencies_set.all()
    county_kml = county.make_kml()
    county_raw = make_kml(county_kml + make_folder(Consts, "Consituencies"))
    f = open(county_name+".kml", "w")
    f.write(county_raw)
    f.close()
    for const in Consts:
        const_name = re.sub("/", " ", const.name)+" CONSTITUENCY"
        const_kml = const.make_kml()
        os.mkdir(const_name)
        os.chdir(const_name)
        wards = const.wards_set.all()
        const_raw = make_kml(const_kml+make_folder(wards, "Wards"))
        f = open(const_name+".kml", "w")
        f.write(const_raw)
        f.close()
        for ward in wards:
            ward_kml = ward.make_kml()
            ward_name = re.sub("/", " ", ward.name)+" WARD"
            os.mkdir(ward_name)
            os.chdir(ward_name)
            stations = ward.stations_set.filter(geom__within=county_geom)
            raw = make_kml(ward_kml+make_folder(stations, "Polling stations"))
            f = open(ward_name+" PollingStations.kml", "w")
            f.write(raw)
            f.close()
            os.chdir("..")
        os.chdir("..")
    os.chdir("..")
                        
            
