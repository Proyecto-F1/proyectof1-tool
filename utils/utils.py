import pandas as pd
import random

circuits_df = pd.read_csv('../data/circuits.csv')
drivers_df = pd.read_csv('../data/drivers.csv')
constructors_df = pd.read_csv('../data/constructors.csv')
races_df = pd.read_csv('../data/races.csv')

def get_circuits_options():
    circuits_options = []

    for row in circuits_df.iterrows():
        row_df = pd.DataFrame(row[1]).transpose().reset_index().iloc[0]

        circuits_options.append(
            {'label': row_df['name'], 'value': row_df['circuitId']},
        )

    return circuits_options

def get_drivers_options():
    drivers_options = []

    for row in drivers_df.iterrows():
        row_df = pd.DataFrame(row[1]).transpose().reset_index().iloc[0]

        drivers_options.append(
            {'label': row_df['forename'] + ' ' + row_df['surname'], 'value': row_df['driverId']},
        )

    return drivers_options

def validate_prediction(result):
    if None in result['qualifying'] or None in result.values():
        return False

    if len(set(result['qualifying'])) != 20:
        return False

    if result['temperature'] < 0 or result['temperature'] > 50:
        return False
        
    if result['circuit'] not in circuits_df['circuitId'].values:
        return False
    
    for qualifying in result['qualifying']:
        if qualifying not in drivers_df['driverId'].values:
            return False

    if len(result['qualifying']) != len(set(result['qualifying'])):
        return False

    if result['precipitation'] < 0 or result['precipitation'] > 100:
        return False

    return True

def build_prediction_df(result):
    result_df = pd.DataFrame()

    result_df['driverId'] = result['qualifying']
    result_df['grid'] = [i for i in range(1, 21)]
    result_df['temp'] = result['temperature']
    result_df['circuitId'] = result['circuit']
    result_df['precipitation'] = result['precipitation']
    result_df['raceId'] = races_df['raceId'].max() + 1
    result_df['constructorId'] = random.choices(constructors_df['constructorId'].values, k=20)
    result_df['statusId'] = 1

    result_df.reset_index(drop=True, inplace=True)

    return result_df

def predict_algorithm(result_df):
    positions = []

    for row in result_df.iterrows():
        row_df = pd.DataFrame(row[1]).transpose().reset_index().iloc[0]

        score = row_df['grid'] * 0.5 + row_df['temp'] * 0.1 + row_df['precipitation'] * 0.4

        positions.append(
            {'driverId': row_df['driverId'], 'score': score},
        )
    
    positions = sorted(positions, key=lambda k: k['score'], reverse=True)

    for i in range(len(positions)):
        positions[i]['position'] = i + 1

    return positions

def get_prediction():
    pass

def get_driver_data():
    pass
