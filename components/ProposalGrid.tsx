import React from 'react';
import { View, StyleSheet } from 'react-native';
import ProposalItem, { Proposal } from './ProposalItem';
import { FlatGrid } from 'react-native-super-grid';

export interface Props {
    proposals: Proposal[]
}

export default function ProposalGrid(props: Props) {
    const renderProposal = (item: any, color: any) => {
        return (
            <ProposalItem text={item.text} power={item.power} color={color} />
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
                renderItem={({ item, index }) => renderProposal(item, colors[index])}
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