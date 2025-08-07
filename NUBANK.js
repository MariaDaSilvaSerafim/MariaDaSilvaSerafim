import React, { useState } from 'react';
import {SafeAreaView, Text, View, StyleSheet} from 'react-native';
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons';

export default function App() {
  return (

    <SafeAreaView style={styles.container}>

      <View style={styles.espaco}>
        <View style={styles.user}>
          <MaterialCommunityIcons name="account"
          size={40} color='#b189d9'/>
        </View>

          <MaterialCommunityIcons name="eye"
          size={40} color='#b189d9'/>

          <MaterialCommunityIcons name="question"
          size={40} color='#b189d9'/>

          <MaterialCommunityIcons name="email"
          size={40} color='#b189d9'/>
      </View>

      <View style={styles.c1}>
        
      </View>

      <View style={styles.c2}>

      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#ecf0f1',
    padding: 1,
  },

  espaco: {
    backgroundColor: '#8b1ccc',
  },

  c1: {
    width: 'auto',
    height: 200,
    backgroundColor: '#8b1ccc',
    padding: 40,
  },

  user: {
    width: 50,
    height: 50,
    backgroundColor: '#ffffff',
    borderRadius: 100,
  },

  c2: {
    width: 'auto',
    height: 250,
    backgroundColor: '#ffffff',
  },
});
