import React from 'react';
import { View, Text, StyleSheet, TouchableHighlight } from 'react-native';
import { FontAwesomeIcon } from '@fortawesome/react-native-fontawesome';
import { faGavel } from '@fortawesome/free-solid-svg-icons'

export interface Props {
    text: string;
    power: number;
    color: string;
    username: string;
    electionId: number;
}

export interface Proposal {
    text: string;
    power: number;
}

export default function ProposalItem(props: Props) {
    const onPress = () => {
        // do something
        const base_url = "http://localhost:8000/api/elections/"
        const vote_url = `${base_url}${props.electionId}/vote`
        const vote_data = {
            username: props.username,
            option: props.text,
            power: 10
        }
        fetch(vote_url, {
            method: "POST",
            body: JSON.stringify(vote_data)
        })
    }
    return (
        <TouchableHighlight onPress={onPress}>
            <View style={[styles.container, { backgroundColor: props.color }]}>
                <Text style={[styles.text, styles.choiceText]}> {props.text} </Text>
                <View style={styles.gavelContainer}>
                    <Text style={[styles.text, styles.powerText]}> {props.power}</Text>
                    <FontAwesomeIcon style={styles.gavelIcon} icon={ faGavel } size={30} />

                </View>
            </View>
        </TouchableHighlight>
    );
}

const styles = StyleSheet.create({
    "container": {
        flex: 1,
        height: 200,
        justifyContent: "space-around"
    },
    "text": {
        textTransform: "capitalize",
        fontWeight: "bold",
        fontSize: 18
    },
    "choiceText": {
        padding: 6,
        textAlign: "center"
    },
    "powerText": {
        padding: 6,
        fontSize: 30,
    },
    "gavelContainer": {
        flexDirection: "row",
        padding: 6,
        justifyContent: "center"
    },
    "gavelIcon": {
        padding: 6,
        marginTop: 6
    }
});