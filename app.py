import streamlit as st
import { useState } from 'react'
import { Button } from "/components/ui/button"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "/components/ui/card"
import { Input } from "/components/ui/input"
import { Label } from "/components/ui/label"
import { Plus, Minus } from "lucide-react"

interface Player {
  name: string
  receptions: number
  receivingYards: number
  rushingYards: number
  passingYards: number
  passingTouchdowns: number
  anytimeTouchdowns: number
}

interface Team {
  wins: number
  losses: number
  totalPoints: number
  totalPointsLost: number
  players: Player[]
}

export default function NFLStatisticsPredictionApp() {
  const [teamA, setTeamA] = useState<Team>({
    wins: 0,
    losses: 0,
    totalPoints: 0,
    totalPointsLost: 0,
    players: [],
  })

  const [teamB, setTeamB] = useState<Team>({
    wins: 0,
    losses: 0,
    totalPoints: 0,
    totalPointsLost: 0,
    players: [],
  })

  const [predictions, setPredictions] = useState<{ gameOutcome: string, playerProps: string[] } | null>(null)

  const addPlayer = (team: 'A' | 'B') => {
    const newPlayer: Player = {
      name: '',
      receptions: 0,
      receivingYards: 0,
      rushingYards: 0,
      passingYards: 0,
      passingTouchdowns: 0,
      anytimeTouchdowns: 0,
    }

    if (team === 'A') {
      setTeamA({ ...teamA, players: [...teamA.players, newPlayer] })
    } else {
      setTeamB({ ...teamB, players: [...teamB.players, newPlayer] })
    }
  }

  const removePlayer = (team: 'A' | 'B', index: number) => {
    if (team === 'A') {
      setTeamA({ ...teamA, players: teamA.players.filter((_, i) => i !== index) })
    } else {
      setTeamB({ ...teamB, players: teamB.players.filter((_, i) => i !== index) })
    }
  }

  const handleTeamChange = (team: 'A' | 'B', field: keyof Team, value: number) => {
    if (team === 'A') {
      setTeamA({ ...teamA, [field]: value })
    } else {
      setTeamB({ ...teamB, [field]: value })
    }
  }

  const handlePlayerChange = (team: 'A' | 'B', index: number, field: keyof Player, value: number | string) => {
    const players = team === 'A' ? teamA.players : teamB.players
    const updatedPlayers = players.map((player, i) => {
      if (i === index) {
        return { ...player, [field]: value }
      }
      return player
    })

    if (team === 'A') {
      setTeamA({ ...teamA, players: updatedPlayers })
    } else {
      setTeamB({ ...teamB, players: updatedPlayers })
    }
  }

  const predict = () => {
    // Simulate prediction logic
    const gameOutcome = teamA.wins > teamB.wins ? 'Team A wins' : 'Team B wins'
    const playerProps = [
      `Player A1 from Team A is predicted to score 2 touchdowns`,
      `Player B2 from Team B is predicted to have 100 receiving yards`,
    ]

    setPredictions({ gameOutcome, playerProps })
  }

  return (
    <div className="p-4">
      <Card className="mb-4">
        <CardHeader>
          <CardTitle>Team A Statistics</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-2 gap-4">
            <div>
              <Label htmlFor="teamA-wins">Wins</Label>
              <Input
                id="teamA-wins"
                type="number"
                value={teamA.wins}
                onChange={(e) => handleTeamChange('A', 'wins', parseInt(e.target.value))}
              />
            </div>
            <div>
              <Label htmlFor="teamA-losses">Losses</Label>
              <Input
                id="teamA-losses"
                type="number"
                value={teamA.losses}
                onChange={(e) => handleTeamChange('A', 'losses', parseInt(e.target.value))}
              />
            </div>
            <div>
              <Label htmlFor="teamA-totalPoints">Total Points</Label>
              <Input
                id="teamA-totalPoints"
                type="number"
                value={teamA.totalPoints}
                onChange={(e) => handleTeamChange('A', 'totalPoints', parseInt(e.target.value))}
              />
            </div>
            <div>
              <Label htmlFor="teamA-totalPointsLost">Total Points Lost</Label>
              <Input
                id="teamA-totalPointsLost"
                type="number"
                value={teamA.totalPointsLost}
                onChange={(e) => handleTeamChange('A', 'totalPointsLost', parseInt(e.target.value))}
              />
            </div>
          </div>
          <div className="mt-4">
            <Button onClick={() => addPlayer('A')} className="flex items-center">
              <Plus className="mr-2" />
              Add Player
            </Button>
          </div>
          {teamA.players.map((player, index) => (
            <div key={index} className="mt-4">
              <div className="flex items-center justify-between">
                <div>
                  <Label htmlFor={`teamA-player-${index}-name`}>Player {index + 1} Name</Label>
                  <Input
                    id={`teamA-player-${index}-name`}
                    value={player.name}
                    onChange={(e) => handlePlayerChange('A', index, 'name', e.target.value)}
                  />
                </div>
                <Button onClick={() => removePlayer('A', index)} className="flex items-center">
                  <Minus className="mr-2" />
                  Remove
                </Button>
              </div>
              <div className="grid grid-cols-2 gap-4 mt-2">
                <div>
                  <Label htmlFor={`teamA-player-${index}-receptions`}>Receptions</Label>
                  <Input
                    id={`teamA-player-${index}-receptions`}
                    type="number"
                    value={player.receptions}
                    onChange={(e) => handlePlayerChange('A', index, 'receptions', parseInt(e.target.value))}
                  />
                </div>
                <div>
                  <Label htmlFor={`teamA-player-${index}-receivingYards`}>Receiving Yards</Label>
                  <Input
                    id={`teamA-player-${index}-receivingYards`}
                    type="number"
                    value={player.receivingYards}
                    onChange={(e) => handlePlayerChange('A', index, 'receivingYards', parseInt(e.target.value))}
                  />
                </div>
                <div>
                  <Label htmlFor={`teamA-player-${index}-rushingYards`}>Rushing Yards</Label>
                  <Input
                    id={`teamA-player-${index}-rushingYards`}
                    type="number"
                    value={player.rushingYards}
                    onChange={(e) => handlePlayerChange('A', index, 'rushingYards', parseInt(e.target.value))}
                  />
                </div>
                <div>
                  <Label htmlFor={`teamA-player-${index}-passingYards`}>Passing Yards</Label>
                  <Input
                    id={`teamA-player-${index}-passingYards`}
                    type="number"
                    value={player.passingYards}
                    onChange={(e) => handlePlayerChange('A', index, 'passingYards', parseInt(e.target.value))}
                  />
                </div>
                <div>
                  <Label htmlFor={`teamA-player-${index}-passingTouchdowns`}>Passing Touchdowns</Label>
                  <Input
                    id={`teamA-player-${index}-passingTouchdowns`}
                    type="number"
                    value={player.passingTouchdowns}
                    onChange={(e) => handlePlayerChange('A', index, 'passingTouchdowns', parseInt(e.target.value))}
                  />
                </div>
                <div>
                  <Label htmlFor={`teamA-player-${index}-anytimeTouchdowns`}>Anytime Touchdowns</Label>
                  <Input
                    id={`teamA-player-${index}-anytimeTouchdowns`}
                    type="number"
                    value={player.anytimeTouchdowns}
                    onChange={(e) => handlePlayerChange('A', index, 'anytimeTouchdowns', parseInt(e.target.value))}
                  />
                </div>
              </div>
            </div>
          ))}
        </CardContent>
      </Card>

      <Card className="mb-4">
        <CardHeader>
          <CardTitle>Team B Statistics</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-2 gap-4">
            <div>
              <Label htmlFor="teamB-wins">Wins</Label>
              <Input
                id="teamB-wins"
                type="number"
                value={teamB.wins}
                onChange={(e) => handleTeamChange('B', 'wins', parseInt(e.target.value))}
              />
            </div>
            <div>
              <Label htmlFor="teamB-losses">Losses</Label>
              <Input
                id="teamB-losses"
                type="number"
                value={teamB.losses}
                onChange={(e) => handleTeamChange('B', 'losses', parseInt(e.target.value))}
              />
            </div>
            <div>
              <Label htmlFor="teamB-totalPoints">Total Points</Label>
              <Input
                id="teamB-totalPoints"
                type="number"
                value={teamB.totalPoints}
                onChange={(e) => handleTeamChange('B', 'totalPoints', parseInt(e.target.value))}
              />
            </div>
            <div>
              <Label htmlFor="teamB-totalPointsLost">Total Points Lost</Label>
              <Input
                id="teamB-totalPointsLost"
                type="number"
                value={teamB.totalPointsLost}
                onChange={(e) => handleTeamChange('B', 'totalPointsLost', parseInt(e.target.value))}
              />
            </div>
          </div>
          <div className="mt-4">
            <Button onClick={() => addPlayer('B')} className="flex items-center">
              <Plus className="mr-2" />
              Add Player
            </Button>
          </div>
          {teamB.players.map((player, index) => (
            <div key={index} className="mt-4">
              <div className="flex items-center justify-between">
                <div>
                  <Label htmlFor={`teamB-player-${index}-name`}>Player {index + 1} Name</Label>
                  <Input
                    id={`teamB-player-${index}-name`}
                    value={player.name}
                    onChange={(e) => handlePlayerChange('B', index, 'name', e.target.value)}
                  />
                </div>
                <Button onClick={() => removePlayer('B', index)} className="flex items-center">
                  <Minus className="mr-2" />
                  Remove
                </Button>
              </div>
              <div className="grid grid-cols-2 gap-4 mt-2">
                <div>
                  <Label htmlFor={`teamB-player-${index}-receptions`}>Receptions</Label>
                  <Input
                    id={`teamB-player-${index}-receptions`}
                    type="number"
                    value={player.receptions}
                    onChange={(e) => handlePlayerChange('B', index, 'receptions', parseInt(e.target.value))}
                  />
                </div>
                <div>
                  <Label htmlFor={`teamB-player-${index}-receivingYards`}>Receiving Yards</Label>
                  <Input
                    id={`teamB-player-${index}-receivingYards`}
                    type="number"
                    value={player.receivingYards}
                    onChange={(e) => handlePlayerChange('B', index, 'receivingYards', parseInt(e.target.value))}
                  />
                </div>
                <div>
                  <Label htmlFor={`teamB-player-${index}-rushingYards`}>Rushing Yards</Label>
                  <Input
                    id={`teamB-player-${index}-rushingYards`}
                    type="number"
                    value={player.rushingYards}
                    onChange={(e) => handlePlayerChange('B', index, 'rushingYards', parseInt(e.target.value))}
                  />
                </div>
                <div>
                  <Label htmlFor={`teamB-player-${index}-passingYards`}>Passing Yards</Label>
                  <Input
                    id={`teamB-player-${index}-passingYards`}
                    type="number"
                    value={player.passingYards}
                    onChange={(e) => handlePlayerChange('B', index, 'passingYards', parseInt(e.target.value))}
                  />
                </div>
                <div>
                  <Label htmlFor={`teamB-player-${index}-passingTouchdowns`}>Passing Touchdowns</Label>
                  <Input
                    id={`teamB-player-${index}-passingTouchdowns`}
                    type="number"
                    value={player.passingTouchdowns}
                    onChange={(e) => handlePlayerChange('B', index, 'passingTouchdowns', parseInt(e.target.value))}
                  />
                </div>
                <div>
                  <Label htmlFor={`teamB-player-${index}-anytimeTouchdowns`}>Anytime Touchdowns</Label>
                  <Input
                    id={`teamB-player-${index}-anytimeTouchdowns`}
                    type="number"
                    value={player.anytimeTouchdowns}
                    onChange={(e) => handlePlayerChange('B', index, 'anytimeTouchdowns', parseInt(e.target.value))}
                  />
                </div>
              </div>
            </div>
          ))}
        </CardContent>
      </Card>

      <div className="flex justify-center">
        <Button onClick={predict}>Predict</Button>
      </div>

      {predictions && (
        <Card className="mt-4">
          <CardHeader>
            <CardTitle>Predictions</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="mb-2"><strong>Game Outcome:</strong> {predictions.gameOutcome}</p>
            <p><strong>Player Props:</strong></p>
            <ul>
              {predictions.playerProps.map((prop, index) => (
                <li key={index}>{prop}</li>
              ))}
            </ul>
          </CardContent>
        </Card>
      )}
    </div>
  )
}
