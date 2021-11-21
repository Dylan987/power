import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import VoteScreen from './components/VoteScreen';

export default function App() {
  const sampleData = {
    "user_power": 80,
    "proposals": [
      {
        "text": "football",
        "power": 20
      },
      {
        "text": "baseball",
        "power": 20
      },
      {
        "text": "ice skating",
        "power": 30
      },
      {
        "text": "hockey",
        "power": 40
      },
    ] 
  }
  return (
    <VoteScreen user_power={sampleData.user_power} proposals={sampleData.proposals}/>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#daf',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
