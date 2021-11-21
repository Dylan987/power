import React, { useState } from 'react';
import { StyleSheet } from 'react-native';
import VoteScreen from './components/VoteScreen';
import { Proposal } from './components/ProposalItem';
import useInterval from './hooks/useInterval'

export interface State {
  user_power: number;
  proposals: Proposal[];
  election_id: number;
}

export default function App() {
  const unchangingSampleData = {
    "username": "dylan",
    "group_name": "friends",
  }

  
  const [data, setData] = useState<State>({
    user_power: 80,
    election_id: 0,
    proposals: [
      {
        text: "hockey",
        power: 20,
      },
      {
        text: "baseball",
        power: 20,
      },
      {
        text: "football",
        power: 20,
      },
      {
        text: "soccer",
        power: 20,
      },
    ]
  });

  useInterval(() => {
    const base_url = "http://localhost:8000/api/"
    const user_url = `${base_url}users/dylan/list`
    let election_id = 0
    let newData = data
    fetch(user_url)
      .then(res => res.json())
      .then((res_data) => {
        newData.user_power = res_data['data']['groups'][0]['power']
        election_id = res_data['data']['groups'][0]['election_id']
        newData.election_id = election_id
      })
      .then(() => {
        fetch(`${base_url}elections/${election_id}`)
          .then(res => res.json())
          .then((res_data) => {
            newData.proposals = res_data['data']['proposals']
            setData({...newData})
          })
      })
  }, 3000)


  return (
    <VoteScreen {...unchangingSampleData} {...data}/>
  );
}
