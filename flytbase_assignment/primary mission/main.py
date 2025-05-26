from data_ingestion import generate_paths, Mission
from temporal_check import interpolate_path
from spatial_check import check_conflicts
from visualization import plot_paths

if __name__ == "__main__":
    primary_wp, intruder_wp = generate_paths()
    primary = Mission(primary_wp)
    intruder = Mission(intruder_wp)

    conflict_free, conflicts = check_conflicts(primary, [intruder])
    print("Conflict Free:", conflict_free)
    if not conflict_free:
        print(f"Conflicts Found: {len(conflicts)}")

    plot_paths(primary_wp, [intruder_wp])
