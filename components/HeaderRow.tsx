import React from 'react';
import { View, StyleSheet, Text } from 'react-native';

import { FontAwesomeIcon } from '@fortawesome/react-native-fontawesome';
import { faGavel } from '@fortawesome/free-solid-svg-icons'

export interface Props {
    user_power: number;
}

export default function HeaderRow (props: Props) {
    return (
        <View style={styles.rightFloat}>
            <FontAwesomeIcon icon={ faGavel } size={28}></FontAwesomeIcon>
            <Text style={styles.powerLabel}>
                {props.user_power}
            </Text>
        </View>
    );
}

const styles = StyleSheet.create({
    "rightFloat": {
        flexDirection: "row-reverse",
        flexGrow: 0,
        marginTop: 30,
        marginHorizontal: 10,
        marginBottom: 10,
        alignItems: "center"
    },
    "powerLabel": {
        padding: 4,
        fontWeight: "bold",
        fontSize: 24
    },
    "gavelIcon": {
        padding: 8,
        marginTop: 3
    }
});