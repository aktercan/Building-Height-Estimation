import math

def calculate_pixel_size(gsd, flying_height):
    """
    Calculate the pixel size in meters.
    
    :param gsd: Ground Sampling Distance in meters.
    :param flying_height: Drone flying height in meters.
    :return: Pixel size in meters.
    """
    return gsd / flying_height

def calculate_distances(pixel_coordinates, pixel_size):
    """
    Calculate the distances in meters between consecutive pixel pairs.
    
    :param pixel_coordinates: List of pixel coordinates (x, y).
    :param pixel_size: Pixel size in meters.
    :return: List of distances in meters.
    """
    return [
        math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * pixel_size
        for (x1, y1), (x2, y2) in zip(pixel_coordinates, pixel_coordinates[1:])
    ]

def calculate_average_distance(distances):
    """
    Calculate the average distance from a list of distances.
    
    :param distances: List of distances in meters.
    :return: Average distance in meters.
    """
    return sum(distances) / len(distances)

def estimate_building_height(average_distance, flying_height):
    """
    Estimate the building height using the average distance and flight height.
    
    :param average_distance: Average distance in meters.
    :param flying_height: Drone flying height in meters.
    :return: Estimated building height in meters.
    """
    return average_distance * flying_height

# Main workflow
def main():
    # Given parameters
    flying_height = 900  # in meters
    gsd = 0.08  # in meters (8 cm)
    pixel_coordinates = [
        (2938.3452497870217, 2484.7347824591498),
        (2743.213186527079, 2508.085141001929),
        (2710.216496287416, 2253.0345881900257),
        (2760.9366348076373, 2247.452531144176),
        (2725.3505760252447, 1952.197743758674),
        (2604.165932604981, 1968.1017329853264),
        (2593.5796075680564, 1882.5592302232726),
        (2862.391769630859, 1851.7166617644239),
        (2938.3452497870217, 2484.7347824591498)
    ]

    # Step 1: Calculate pixel size
    pixel_size = calculate_pixel_size(gsd, flying_height)

    # Step 2: Calculate distances between pixel pairs
    distances = calculate_distances(pixel_coordinates, pixel_size)

    # Step 3: Calculate average distance
    average_distance = calculate_average_distance(distances)

    # Step 4: Estimate building height
    building_height = estimate_building_height(average_distance, flying_height)

    print(f"Pixel size: {pixel_size:.6f} meters")
    print(f"Distances between pixel pairs: {distances}")
    print(f"Average distance: {average_distance:.2f} meters")
    print(f"Estimated building height: {building_height:.2f} meters")

# Run the main function
if __name__ == "__main__":
    main()