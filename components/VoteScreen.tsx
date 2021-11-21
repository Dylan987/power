import React from 'react';
import { View, StyleSheet } from 'react-native';
import HeaderRow from './HeaderRow';
import ProposalGrid from './ProposalGrid';
import { Proposal } from './ProposalItem';

interface Props {
    user_power: number;
    proposals: Proposal[];
}

export default function VoteScreen(props: Props) {
    return (
        <View style={styles.container}>
            <HeaderRow user_power={props.user_power} />
            <ProposalGrid proposals={props.proposals} />
        </View>
    );
}

const styles = StyleSheet.create({
    "container": {
        backgroundColor: "#dfc0eb",
        flex: 1
    }
});