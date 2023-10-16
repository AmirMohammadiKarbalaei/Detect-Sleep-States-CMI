import pandas as pd





def Categorize_hours(data, num_categories):
    category_size = 24 // num_categories
    
    categories = []
    
    for hour in data.hour:
        category_label = hour // category_size
        categories.append(f"{category_label}")
    int8_list = [int(value) for value in categories]
    data_quartile = pd.DataFrame(int8_list,columns=["day_quartile"])
    return pd.concat([data,data_quartile],axis =1)


def add_features(data):
    data["day of year"] = data.timestamp.dt.dayofyear
    data["day of week"] = data.timestamp.dt.day_of_week #can also do day_name() for the name of the day
    data["month"] = data.timestamp.dt.month # can do month_name() for 
    data["days in month"] = data.timestamp.dt.days_in_month
    data["minute"] = data.timestamp.dt.minute
    return data







def Create_lag_features(data, window_size,data_name1,data_name2):
    data_frame1 = pd.DataFrame(data[data_name1])
    for i in range(1, window_size+1):
        data_frame1[f'{data_name1} lag_{i}'] = data_frame1[data_name1].shift(i)
    data_frame1 = data_frame1.drop(data_name1,axis= 1)

    data_frame2 = pd.DataFrame(data[data_name2])
    for i in range(1, window_size+1):
        data_frame2[f'{data_name2} lag_{i}'] = data_frame2[data_name2].shift(i)
    data_frame2 = data_frame2.drop(data_name2,axis= 1)


    return pd.concat([data_frame1,data_frame2],axis =1 )



def Create_rolling_and_expanding_statistics(data, window_size, data_name):
    rolling_stats = data[f"{data_name}"].rolling(window=window_size)
    expanding_stats = data[f"{data_name}"].expanding(min_periods=1)

    rolling_Data = pd.DataFrame({
        f"{data_name} rolling mean": rolling_stats.mean().astype("float16"), # can also add diff of this windows  mean to the previous windows mean
        f"{data_name} rolling std": rolling_stats.std().astype("float16"),
        f"{data_name} rolling median": rolling_stats.median().astype("float16"),
        f"{data_name} rolling max": rolling_stats.max().astype("float16"),
        f"{data_name} rolling min": rolling_stats.min().astype("float16")
    })

    expanding_Data = pd.DataFrame({
        f"{data_name} expanding mean": expanding_stats.mean().astype("float16"),
        f"{data_name} expanding std": expanding_stats.std().astype("float16"),
        f"{data_name} expanding median": expanding_stats.median().astype("float16"),
        f"{data_name} expanding max": expanding_stats.max().astype("float16"),
        f"{data_name} expanding min": expanding_stats.min().astype("float16")
    })
    rolling_Data = rolling_Data.drop(f"{data_name}")
    expanding_Data = expanding_Data.drop(f"{data_name}")
    
    return pd.concat([data,rolling_Data,expanding_Data],axis = 1)