import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { FontAwesomeIcon } from '@fortawesome/react-native-fontawesome';
import { faGavel } from '@fortawesome/free-solid-svg-icons'

export interface Props {
    text: string;
    power: number;
    color: string;
}

export interface Proposal {
    text: string;
    power: number;
}

export default function ProposalItem(props: Props) {
    return (
        <View style={[styles.container, { backgroundColor: props.color }]}>
            <Text style={[styles.text, styles.choiceText]}> {props.text} </Text>
            <View style={styles.gavelContainer}>
                <Text style={[styles.text, styles.powerText]}> {props.power}</Text>
                <FontAwesomeIcon style={styles.gavelIcon} icon={ faGavel } size={20} />

            </View>
        </View>
    );
}

const styles = StyleSheet.create({
    "container": {
        flex: 1
    },
    "text": {
        textTransform: "capitalize",
        fontWeight: "bold",
        fontSize: 16
    },
    "choiceText": {
        padding: 6,
        textAlign: "center"
    },
    "powerText": {
        padding: 6,
        fontSize: 20,
    },
    "gavelContainer": {
        flexDirection: "row",
        padding: 6,
        justifyContent: "center"
    },
    "gavelIcon": {
        padding: 6,
        size: 20,
        marginTop: 4
    }
});