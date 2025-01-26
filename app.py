import streamlit as st

# Define data structures
class Player:
    def __init__(self, name="", receptions=0, receiving_yards=0, rushing_yards=0,
                 passing_yards=0, passing_touchdowns=0, anytime_touchdowns=0):
        self.name = name
        self.receptions = receptions
        self.receiving_yards = receiving_yards
        self.rushing_yards = rushing_yards
        self.passing_yards = passing_yards
        self.passing_touchdowns = passing_touchdowns
        self.anytime_touchdowns = anytime_touchdowns

class Team:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.total_points = 0
        self.total_points_lost = 0
        self.players = []

# Initialize session state for teams
if "teamA" not in st.session_state:
    st.session_state.teamA = Team()
if "teamB" not in st.session_state:
    st.session_state.teamB = Team()
if "predictions" not in st.session_state:
    st.session_state.predictions = None

# Function to add a player to a team
def add_player(team):
    team.players.append(Player())

# Function to remove a player from a team
def remove_player(team, index):
    if 0 <= index < len(team.players):
        team.players.pop(index)

# Prediction logic
def predict():
    teamA = st.session_state.teamA
    teamB = st.session_state.teamB
    outcome = "Team A wins" if teamA.wins > teamB.wins else "Team B wins"
    player_props = [
        "Player A1 from Team A is predicted to score 2 touchdowns",
        "Player B2 from Team B is predicted to have 100 receiving yards",
    ]
    st.session_state.predictions = {"gameOutcome": outcome, "playerProps": player_props}

# Input forms for teams
for team_name, team in [("Team A", st.session_state.teamA), ("Team B", st.session_state.teamB)]:
    st.header(f"{team_name} Statistics")
    team.wins = st.number_input(f"{team_name} Wins", value=team.wins, step=1)
    team.losses = st.number_input(f"{team_name} Losses", value=team.losses, step=1)
    team.total_points = st.number_input(f"{team_name} Total Points", value=team.total_points, step=1)
    team.total_points_lost = st.number_input(f"{team_name} Total Points Lost", value=team.total_points_lost, step=1)

    st.subheader(f"{team_name} Players")
    for i, player in enumerate(team.players):
        with st.expander(f"Player {i + 1}"):
            player.name = st.text_input(f"Player {i + 1} Name", value=player.name)
            player.receptions = st.number_input(f"Player {i + 1} Receptions", value=player.receptions, step=1)
            player.receiving_yards = st.number_input(f"Player {i + 1} Receiving Yards", value=player.receiving_yards, step=1)
            player.rushing_yards = st.number_input(f"Player {i + 1} Rushing Yards", value=player.rushing_yards, step=1)
            player.passing_yards = st.number_input(f"Player {i + 1} Passing Yards", value=player.passing_yards, step=1)
            player.passing_touchdowns = st.number_input(f"Player {i + 1} Passing Touchdowns", value=player.passing_touchdowns, step=1)
            player.anytime_touchdowns = st.number_input(f"Player {i + 1} Anytime Touchdowns", value=player.anytime_touchdowns, step=1)
        if st.button(f"Remove Player {i + 1} from {team_name}"):
            remove_player(team, i)

    if st.button(f"Add Player to {team_name}"):
        add_player(team)

# Prediction button
if st.button("Predict"):
    predict()

# Display predictions
if st.session_state.predictions:
    st.subheader("Predictions")
    st.write(f"**Game Outcome:** {st.session_state.predictions['gameOutcome']}")
    st.write("**Player Props:**")
    st.write("\n".join(st.session_state.predictions["playerProps"]))
