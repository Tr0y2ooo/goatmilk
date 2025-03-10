"""Simple Travelling Salesperson Problem (TSP) between cities."""

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import requests
import json
import pandas as pd

API_KEY = "APIKEY"

file_path = "a.xlsx"  
df = pd.read_excel(file_path,skiprows=3)

gps_data = df.iloc[:, -1].dropna().tolist()
gps_data = [str(gps).strip() for gps in gps_data]

#print(gps_data)
locations = gps_data

def get_distance_matrix(locations, api_key):
    """使用 Google Distance Matrix API 取得距離矩陣"""
    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"

    # 將座標轉換為 URL 參數
    origins = "|".join(locations)
    destinations = "|".join(locations)

    # 建立請求參數
    params = {
        "origins": origins,
        "destinations": destinations,
        "key": api_key,
        "mode": "driving",  # 可選：walking, bicycling, transit
        "units": "metric",  # 使用公尺（可改 "imperial" 英制）
    }

    # 發送 API 請求
    response = requests.get(base_url, params=params)
    result = response.json()

    # 解析 JSON，轉換為距離矩陣
    distance_matrix = []
    for row in result["rows"]:
        distances = [element["distance"]["value"] for element in row["elements"]]
        distance_matrix.append(distances)

    return distance_matrix

distance_matrix = get_distance_matrix(locations, API_KEY)

distance_matrix_km = [[d / 1000 for d in row] for row in distance_matrix]

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data["distance_matrix"] = distance_matrix_km
    data["num_vehicles"] = 1
    data["depot"] = 0
    return data


def print_solution(manager, routing, solution):
    """Prints solution on console."""
    print(f"Objective: {solution.ObjectiveValue()} miles")
    index = routing.Start(0)
    plan_output = "Route for vehicle 0:\n"
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += f" {manager.IndexToNode(index)} ->"
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += f" {manager.IndexToNode(index)}\n"
    print(plan_output)
    plan_output += f"Route distance: {route_distance}miles\n"


def main():
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(
        len(data["distance_matrix"]), data["num_vehicles"], data["depot"]
    )

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data["distance_matrix"][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(manager, routing, solution)


if __name__ == "__main__":
    main()
