# Mez Planner

![image](https://github.com/user-attachments/assets/4519c47c-4e70-4eda-9176-b9bc55f5e141)


## Project Description

**Mez Planner** is a web application under development aimed at helping users plan and visualize their daily tasks. The application will feature a customizable time ruler where users can add tasks, and these tasks will be reflected both on the time ruler and on a pie chart that displays time distribution.

This project is designed to showcase skills in Python, SQL, and Data Science, using technologies such as React for the frontend and Flask for the backend.

## Planned Features

- Task addition with customizable time intervals.
- Display of tasks on the time ruler, with color-coded representation for each task.
- Visualization of tasks in a pie chart showing the time distribution throughout the day.
- Storage of daily task data in a database for future analysis.
- (Future) User login system.

## Technologies Used

- **Frontend**: React
- **Backend**: Flask (Python)
- **Database**: To be decided
- **Python Libraries**:
  - Flask
  - Pandas
  - Matplotlib
- **Development Environment**: 
  - Nix for environment management
  - Code linting and quality tools such as Flake8, Pyflakes, and Black

## Development Environment Setup

This project uses Nix to configure the development environment. You can set up the project locally by running the flake manually or using `direnv` for convenience.

### Prerequisites

- **Nix**: Install Nix by following the official instructions [here](https://nixos.org/download.html).

### How to Set Up the Environment

1. Clone the repository:
    ```bash
    git clone https://github.com/Menezess42/MezPlanner.git
    cd MezPlanner
    ```

2. Set up the environment using Nix:
    ```bash
    nix develop
    ```

Alternatively, if you are using `direnv`, simply run:
    ```bash
    direnv allow
    ```

Both methods will configure the environment as defined in the `flake.nix` file, installing all necessary dependencies.
