from data_ingestion import create_simulated_dataset

if __name__ == "__main__":
    simulated_missions = create_simulated_dataset()
    for mission in simulated_missions:
        print(f"Drone: {mission.drone_id}")
        for wp in mission.waypoints:
            print(f"  Waypoint: ({wp.x:.2f}, {wp.y:.2f}, {wp.z:.2f}, t={wp.t:.1f})")
