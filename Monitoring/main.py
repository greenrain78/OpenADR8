import ast

from DoMonit.domonit.events import Events


def print_events(docker_data: dict):
    if docker_data['Type'] == 'container':
        print(f"name {docker_data['Actor']['Attributes']['name']}")
        print(f"status {docker_data['status']}")
        print(f"exitCode {docker_data['Actor']['Attributes']['exitCode']}")


if __name__ == "__main__":
    print("main run")
    e = Events()
    events = e.events()
    print(f"start for {type(events)} - {events}")

    for event in events:
        data = event.decode('utf-8')
        convert_data = ast.literal_eval(data)
        for key, val in convert_data.items():
            print(f"{key}: {val}")
        # print_events(convert_data)

        # print(f"status {convert_data['status']}")
        # print(f"Type {convert_data['Type']}")
        # print(f"from {convert_data['from']}")
        # print(f"action {convert_data['Action']}")
        #
        # print(f"name {convert_data['Actor']['Attributes']['name']}")

        print("for end -------------------------------------------------------")
