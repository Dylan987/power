import React from 'react';
import { View, StyleSheet } from 'react-native';
import ProposalItem, { Proposal } from './ProposalItem';
import { FlatGrid } from 'react-native-super-grid';

export interface Props {
    username: string;
    election_id: number;
    group_name: string;
    proposals: Proposal[]
}

export default function ProposalGrid(props: Props) {
    const renderProposal = (item: any, color: any, username: any, election_id: number) => {
        return (
            <ProposalItem {...item} color={color} username={username} electionId={election_id} />
        );
    }

    const colors = [
        "#e01529", // red
        "#dad030", // yellow
        "#1360d0", // blue
        "#26990b", // green
    ]

    return (
        <View style={styles.container}>
            <FlatGrid 
                data={props.proposals}
                renderItem={({ item, index }) => renderProposal(item, colors[index], props.username, props.election_id)}
                spacing={0}
                itemDimension={150}
            />
        </View>
    );
}

const styles = StyleSheet.create({
    "container": {
        flexGrow: 1
    }
});