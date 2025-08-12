import React, { useState } from 'react';
import { SafeAreaView, Text, View, StyleSheet, TouchableOpacity, Image, ScrollView} from 'react-native';
import {MaterialIcons, MaterialCommunityIcons} from '@expo/vector-icons';

export default function App() {
  const [balanceVisible, setBalanceVisible] = useState(false);

  return (
    <SafeAreaView style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <View style={styles.cont}>
          <View style={styles.userIcon}>
            <MaterialCommunityIcons name="account" size={28} color='#fff'/>
          </View>

          <Text style={styles.headerText}>Olá, Maria</Text>
        </View>
        
        <View style={styles.headerIcons}>
          <View style={styles.icons}>
            <TouchableOpacity onPress={() => setBalanceVisible(!balanceVisible)}>
              <MaterialCommunityIcons 
                name={balanceVisible ? "eye": "eye-off"} 
                size={28} 
                color='#fff'
                style={styles.icon}
              />
            </TouchableOpacity>
            <MaterialCommunityIcons name="help-circle" size={28} color='#fff' style={styles.icon}/>
            <MaterialCommunityIcons name="email" size={28} color='#fff' style={styles.icon}/>
          </View>
        </View>
      </View>

      {/* Main Card */}
      <View style={styles.mainCard}>
        <Text style={styles.cardTitle}>Conta</Text>
        
        <View style={styles.balanceContainer}>
          <Text style={styles.currencySymbol}>R$</Text>
          <Text style={styles.balance}>
            {balanceVisible ? "9.876,54" : "••••,••"}
          </Text>
        </View>
        
        <Text style={styles.cardFooter}>Saldo disponível</Text>
        
      <ScrollView horizontal={true} showsHorizontalScrollIndicator={false}>
        <View style={styles.cardActions}>
          <TouchableOpacity style={styles.actionButton}>
            <MaterialCommunityIcons name="qrcode-scan" size={24} color='#fff'/>
            <Text style={styles.actionText}>Área Pix</Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.actionButton}>
            <MaterialCommunityIcons name="barcode" size={24} color='#fff'/>
            <Text style={styles.actionText}>Pagar</Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.actionButton}>
            <MaterialCommunityIcons name="barcode" size={24} color='#fff'/>
            <Text style={styles.actionText}>Pagar</Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.actionButton}>
            <MaterialIcons name="swap-horiz" size={24} color='#fff'/>
            <Text style={styles.actionText}>Transferir</Text>
          </TouchableOpacity>
          
          <TouchableOpacity style={styles.actionButton}>
            <MaterialCommunityIcons name="cash-plus" size={24} color='#fff'/>
            <Text style={styles.actionText}>Depositar</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
      </View>

      {/* Credit Card Section */}
      <View style={styles.creditCardSection}>
        <View style={styles.sectionHeader}>
        <MaterialIcons name="style" size={24} color='#fff'/>
          <Text style={styles.sectionTitle}>Cartão de crédito</Text>
        </View>
      </View>

      {/* Discover Section */}

      <ScrollView horizontal={true} showsHorizontalScrollIndicator={false} style={styles.containers}>
        <View style={styles.discoverSection}>
          <Text style={styles.discoverTitle}>Invista em <Text style={styles.cor}>CDBs escolhidos pelo {"\n"}Nu</Text>, a partir de R$100.</Text>
        </View>

        <View style={styles.discoverSection}>
          <Text style={styles.discoverTitle}>Invista em <Text style={styles.cor}>CDBs escolhidos pelo {"\n"}Nu</Text>, a partir de R$100.</Text>
        </View>

        <View style={styles.discoverSection}>
          <Text style={styles.discoverTitle}>Invista em <Text style={styles.cor}>CDBs escolhidos pelo {"\n"}Nu</Text>, a partir de R$100.</Text>
        </View>
      </ScrollView>
    </SafeAreaView>
    
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#000',
  },
  
  header: {
    width: 'auto',
    height: 200,
    backgroundColor: '#820ad1',
    paddingTop: 10,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },

  cont: {
    gap: 40,
    margin: 10,
  },

  headerText: {
    color: '#fff',
    fontSize: 20,
    fontWeight: 'bold',
  },

  userIcon: {
    width: 40,
    height: 40,
    backgroundColor: '#9d49d5',
    borderRadius: 20,
    justifyContent: 'center',
    alignItems: 'center',
  },

  headerIcons: {
    margin: 10,
    position: 'absolute',
    top: 48,
    right: 10,
  },

  icons: {
    flexDirection: 'row',
    
  },

  icon: {
    marginLeft: 20,
  },

  mainCard: {
    backgroundColor: '#000',
    padding: 20,
    // marginTop: 40,
  },

  cardTitle: {
    color: '#fff',
    fontSize: 18,
    marginBottom: 20,
  },

  balanceContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 5,
  },

  currencySymbol: {
    color: '#fff',
    fontSize: 24,
    marginRight: 5,
  },

  balance: {
    color: '#fff',
    fontSize: 32,
    fontWeight: 'bold',
  },

  cardFooter: {
    color: 'rgba(255,255,255,0.7)',
    fontSize: 16,
    marginBottom: 25,
  },

  cardActions: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 10,
    gap: 10,
  },

  actionButton: {
    alignItems: 'center',
    backgroundColor: '#393d42',
    padding: 10,
    borderRadius: 50,
    width: 100,
  },

  actionText: {
    color: '#fff',
    fontSize: 14,
    marginTop: 5,
  },

  creditCardSection: {
    backgroundColor: '#393d42',
    borderRadius: 10,
    marginHorizontal: 20,
    width: 320,
    height: 60,
    marginTop: 10,
    alignItems: 'start',
    justifyContent: 'center',
  },

  sectionHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 15,
    gap: 20,
    textAlign: 'center',
    margin: 10,
  },

  sectionTitle: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
  },

  discoverSection: {
    backgroundColor: '#fff',
    margin: 20,
    borderRadius: 12,
    padding: 20,
    marginTop: 10,
    height: 100,
    width: 320,
  },

  discoverTitle: {
    color: '#000',
    fontSize: 18,
    // fontWeight: 'bold',
    marginBottom: 15,
  },

  cor: {
    color: '#820ad1'
  }
});
