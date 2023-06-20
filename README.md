# **Blue_Rabbit**
<!-- Impact of the Green and Yellow Cab in New York City On New York City Traffic while looking at the weather. -->

The impact of Green and Yellow Cabs in New York City and the affects they have on traffic while looking at the weather.

### **Source of Weather Data.**
Open-Meteo - An open-source weather API.
Open Meteo weather forecast APIs use weather models from multiple national weather providers. For each location worldwide, the best models are combined to provide the best possible forecast.
Link to the site [Weather API](https://open-meteo.com/)


### **Source of Green and Yellow Taxi Data.**
NYC Taxi & Limousine Commission - Provides Yellow Taxi and Green Taxi Trip Records.
The data used in the attached datasets were collected and provided to the NYC Tadxi and Limousine Commision (TLC) by technology providers authorized under the Taxicab & Livery Passenger enhancement Programs (TPEP/LPEP).
Link to the site [TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

### **Data Dictonary**
* [Green Taxi Trip Records](data_dictionary_trip_records_green.pdf)
* [Yellow Taxi Trip Records](data_dictionary_trip_records_yellow.pdf)
* [Weather API Records](https://open-meteo.com/en/docs)



### **Green Taxi Column Names and Data Type:**
* Unnamed 0.1:                int64
* Unnamed 0:                  int64
* VendorID:                   int64
* lpep_pickup_datetime:     object
* lpep_dropoff_datetime:    object
* store_and_fwd_flag;        object
* RatecodeID:               float64
* PULocationID:               int64
* DOLocationID:               int64
* passenger_count:          float64
* trip_distance:            float64
* fare_amount:              float64
* extra:                    float64
* mta_tax:                  float64
* tip_amount:               float64
* tolls_amount:             float64
* ehail_fee:                float64
* improvement_surcharge:    float64
* total_amount:             float64
* payment_type:             float64
* trip_type:                float64
* congestion_surcharge:     float64
* dtype:                    object


### **Yellow Taxi Column Names and Data Type:**
* Unnamed 0.1:               int64
* Unnamed 0:                 int64
* VendorID:                   int64
* tpep_pickup_datetime:      object
* tpep_dropoff_datetime:     object
* passenger_count:          float64
* trip_distance:            float64
* RatecodeID:               float64
* store_and_fwd_flag:        object
* PULocationID:               int64
* DOLocationID:               int64
* payment_type:               int64
* fare_amount:              float64
* extra:                    float64
* mta_tax:                  float64
* tip_amount:               float64
* tolls_amount:             float64
* improvement_surcharge:    float64
* total_amount:             float64
* congestion_surcharge:     float64
* airport_fee:              float64
* Airport_fee:              float64
* dtype:                     object

### **Weather Column Names and Data Type:**
* time:                        object
* temperature_2m (°F):        float64
* relativehumidity_2m (%):      int64
* precipitation (inch):       float64
* rain (inch):                float64
* snowfall (inch):            float64
* cloudcover (%):               int64
* windspeed_10m (mp/h):       float64
* dtype:                       object

