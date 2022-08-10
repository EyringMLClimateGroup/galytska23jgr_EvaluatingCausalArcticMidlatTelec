def read_Arctic_vars (data_era5): 
    pv = data_era5.PV.data
    tas = data_era5.Arctic_temperature.data
    qbo = data_era5.QBO.data
    qbo_station = data_era5.QBO_station.data
    sib_slp = data_era5.Psl_Sib.data
    ural_slp = data_era5.Psl_Ural.data
    aleut_slp = data_era5.Psl_Aleut.data
    zon_wind = data_era5.zonal_wind.data
    vlux = data_era5.heat_flux.data
    time = data_era5.time.data
    return pv, tas, qbo, qbo_station, sib_slp, ural_slp, aleut_slp, zon_wind, vlux, time

def read_Arctic_vars_noqbo_tas (data_era5):
    pv = data_era5.PV.data
    tas = data_era5.Arctic_temperature.data
    tas_B = data_era5.Temperature_Baffin.data
    tas_S = data_era5.Temperature_Sib.data
    sib_slp = data_era5.Psl_Sib.data
    ural_slp = data_era5.Psl_Ural.data
    aleut_slp = data_era5.Psl_Aleut.data
    zon_wind = data_era5.zonal_wind.data
    vlux = data_era5.heat_flux.data
    time = data_era5.time.data
    return pv, tas, tas_B, tas_S, sib_slp, ural_slp, aleut_slp, zon_wind, vlux, time


def read_model_data (model_data): 
    pv = model_data.PV.data
    tas = model_data.Arctic_temperature.data
    qbo = model_data.QBO.data
    qbo_station = model_data.QBO_station.data
    sib_slp = model_data.Psl_Sib.data
    ural_slp = model_data.Psl_Ural.data
    aleut_slp = model_data.Psl_Aleut.data
    zon_wind = model_data.zonal_wind.data
    vlux = model_data.heat_flux.data
    BK_sic = model_data.BK_sic.data
    Ok_sic = model_data.Ok_sic.data
    time = model_data.time.data
    return pv, tas, qbo, qbo_station, sib_slp, ural_slp, aleut_slp, zon_wind, vlux, BK_sic, Ok_sic, time

def read_model_data_noqbo_allt (model_data):
    pv = model_data.PV.data
    tas = model_data.Arctic_temperature.data
#    qbo = model_data.QBO.data
#    qbo_station = model_data.QBO_station.data
    tas_B = model_data.Temperature_Baffin.data
    tas_S = model_data.Temperature_Sib.data
    sib_slp = model_data.Psl_Sib.data
    ural_slp = model_data.Psl_Ural.data
    aleut_slp = model_data.Psl_Aleut.data
    zon_wind = model_data.zonal_wind.data
    vlux = model_data.heat_flux.data
    BK_sic = model_data.BK_sic.data
    Ok_sic = model_data.Ok_sic.data
    time = model_data.time.data
    return pv, tas, tas_B, tas_S, sib_slp, ural_slp, aleut_slp, zon_wind, vlux, BK_sic, Ok_sic, time



def read_siconca (model_data): 
    BK_sic = model_data.BK_sic.data
    Ok_sic = model_data.Ok_sic.data

    return BK_sic, Ok_sic
