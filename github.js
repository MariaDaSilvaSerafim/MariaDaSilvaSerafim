import React, { useState } from 'react';
import { SafeAreaView, Text, View, StyleSheet, TouchableOpacity, Image } from 'react-native';
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons';

export default function App() {
  const [balanceVisible, setBalanceVisible] = useState(false);

  return (
    <SafeAreaView style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <View style={styles.userIcon}>
          <MaterialCommunityIcons name="account" size={28} color='#fff'/>
        </View>
        
        <View style={styles.headerIcons}>
          <TouchableOpacity onPress={() => setBalanceVisible(!balanceVisible)}>
            <MaterialCommunityIcons 
              name={balanceVisible ? "eye-off" : "eye"} 
              size={28} 
              color='#fff'
              style={styles.icon}
            />
          </TouchableOpacity>
          <MaterialCommunityIcons name="help-circle" size={28} color='#fff' style={styles.icon}/>
          <MaterialCommunityIcons name="email" size={28} color='#fff' style={styles.icon}/>
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
        
        <View style={styles.cardActions}>
          <TouchableOpacity style={styles.actionButton}>
            <MaterialCommunityIcons name="arrow-up" size={24} color='#820ad1'/>
            <Text style={styles.actionText}>Transferir</Text>
          </TouchableOpacity>
          
          <TouchableOpacity style={styles.actionButton}>
            <MaterialCommunityIcons name="arrow-down" size={24} color='#820ad1'/>
            <Text style={styles.actionText}>Depositar</Text>
          </TouchableOpacity>
          
          <TouchableOpacity style={styles.actionButton}>
            <MaterialCommunityIcons name="barcode" size={24} color='#820ad1'/>
            <Text style={styles.actionText}>Pagar</Text>
          </TouchableOpacity>
        </View>
      </View>

      {/* Credit Card Section */}
      <View style={styles.creditCardSection}>
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>Cartão de crédito</Text>
          <MaterialCommunityIcons name="chevron-right" size={24} color='#820ad1'/>
        </View>
        
        <View style={styles.creditCardInfo}>
          <Text style={styles.creditCardText}>Fatura atual</Text>
          <Text style={styles.creditCardValue}>R$ 1.234,56</Text>
          <Text style={styles.creditCardFooter}>Limite disponível de R$ 8.765,43</Text>
        </View>
      </View>

      {/* Discover Section */}
      <View style={styles.discoverSection}>
        <Text style={styles.discoverTitle}>Descubra mais</Text>
        
        <View style={styles.discoverGrid}>
          <TouchableOpacity style={styles.discoverItem}>
            <View style={styles.discoverIcon}>
              <MaterialCommunityIcons name="cellphone" size={24} color='#820ad1'/>
            </View>
            <Text style={styles.discoverText}>Recarga de celular</Text>
          </TouchableOpacity>
          
          <TouchableOpacity style={styles.discoverItem}>
            <View style={styles.discoverIcon}>
              <MaterialCommunityIcons name="shopping" size={24} color='#820ad1'/>
            </View>
            <Text style={styles.discoverText}>Shopping</Text>
          </TouchableOpacity>
        </View>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  header: {
    backgroundColor: '#820ad1',
    padding: 20,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
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
    flexDirection: 'row',
  },
  icon: {
    marginLeft: 20,
  },
  mainCard: {
    backgroundColor: '#820ad1',
    margin: 20,
    borderRadius: 12,
    padding: 20,
    marginTop: -40,
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
  },
  actionButton: {
    alignItems: 'center',
    backgroundColor: '#fff',
    padding: 10,
    borderRadius: 50,
    width: 100,
  },
  actionText: {
    color: '#820ad1',
    fontSize: 14,
    marginTop: 5,
  },
  creditCardSection: {
    backgroundColor: '#fff',
    marginHorizontal: 20,
    borderRadius: 12,
    padding: 20,
    marginTop: 10,
  },
  sectionHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 15,
  },
  sectionTitle: {
    color: '#000',
    fontSize: 18,
    fontWeight: 'bold',
  },
  creditCardInfo: {
    marginTop: 5,
  },
  creditCardText: {
    color: '#666',
    fontSize: 16,
  },
  creditCardValue: {
    color: '#000',
    fontSize: 24,
    fontWeight: 'bold',
    marginVertical: 5,
  },
  creditCardFooter: {
    color: '#666',
    fontSize: 14,
  },
  discoverSection: {
    backgroundColor: '#fff',
    margin: 20,
    borderRadius: 12,
    padding: 20,
    marginTop: 10,
  },
  discoverTitle: {
    color: '#000',
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 15,
  },
  discoverGrid: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  discoverItem: {
    alignItems: 'center',
    width: '48%',
  },
  discoverIcon: {
    backgroundColor: '#f0e6f9',
    width: 50,
    height: 50,
    borderRadius: 25,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 10,
  },
  discoverText: {
    color: '#820ad1',
    fontSize: 14,
    textAlign: 'center',
  },
});
