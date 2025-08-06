
import React, { useState } from 'react';
import { Text, TextInput, TouchableOpacity, 
SafeAreaView, StyleSheet, View, Animated, 
Easing, Keyboard } from 'react-native';

export default function App() {

  const [peso, setPeso] = useState('');
  const [altura, setAltura] = useState('');
  const [resultado, setResultado] = useState(null);
  const [classificacao, setClassificacao] = useState('');
  const [scaleValue] = useState(new Animated.Value(0));
  const [fadeValue] = useState(new Animated.Value(0));

  const calcularIMC = () => {
    Keyboard.dismiss();
    
    if (!peso || !altura) {
      alert('Por favor, preencha peso e altura');
      return;
    }

    const imc = (parseFloat(peso) / (altura * altura)).toFixed(1);
    setResultado(imc);

  let classificacaoText = '';
    let corClassificacao = '#000';

    if (imc < 18.5) {
      classificacaoText = 'Abaixo do peso';
      corClassificacao = '#3498db';
    } else if (imc < 25) {
      classificacaoText = 'Peso normal';
      corClassificacao = '#2ecc71';
    } else if (imc < 30) {
      classificacaoText = 'Sobrepeso';
      corClassificacao = '#f39c12';
    } else if (imc < 35) {
      classificacaoText = 'Obesidade Grau I';
      corClassificacao = '#e74c3c';
    } else if (imc < 40) {
      classificacaoText = 'Obesidade Grau II';
      corClassificacao = '#c0392b';
    } else {
      classificacaoText = 'Obesidade Grau III';
      corClassificacao = '#7f0000';
    }

    setClassificacao(classificacaoText);

    // Animação
    scaleValue.setValue(0);
    fadeValue.setValue(0);

    Animated.parallel([
      Animated.timing(scaleValue, {
        toValue: 1,
        duration: 500,
        easing: Easing.elastic(1),
        useNativeDriver: true,
      }),
      Animated.timing(fadeValue, {
        toValue: 1,
        duration: 800,
        useNativeDriver: true,
      })
    ]).start();
  };

  const scaleAnimation = scaleValue.interpolate({
    inputRange: [0, 1],
    outputRange: [0.8, 1]
  });

  const fadeAnimation = fadeValue.interpolate({
    inputRange: [0, 1],
    outputRange: [0, 1]
  });

  return (
    <SafeAreaView style={style.container}>
      <View style={style.header}>
        <Text style={style.titulo}>CALCULADORA DE IMC</Text>
        <Text style={style.subtitulo}>Descubra seu Índice de Massa Corporal</Text>
      </View>

      <View style={style.formContainer}>
        <TextInput 
          style={style.input}
          placeholder="Peso (kg) - Ex. 84"
          keyboardType="numeric"
          value={peso}
          onChangeText={setPeso}
          placeholderTextColor="#999"
        />

        <TextInput
          style={style.input} 
          placeholder="Altura (m ou cm) - Ex. 1,83 ou 176"
          keyboardType="numeric"
          value={altura}
          onChangeText={setAltura}
          placeholderTextColor="#999"
        />

        <TouchableOpacity 
          style={style.btn}
          onPress={calcularIMC}
          activeOpacity={0.7}
        >
          <Text style={style.btnText}>CALCULAR IMC</Text>
        </TouchableOpacity>
      </View>

      {resultado && (
        <Animated.View style={[style.resultContainer, {
          opacity: fadeAnimation,
          transform: [{ scale: scaleAnimation }]
        }]}>
          <Text style={style.resultText}>Seu IMC é: {resultado}</Text>
          <Text style={[style.classificacaoText, { color: classificacao.corClassificacao || '#000' }]}>
            {classificacao}
          </Text>
          <View style={style.legendaContainer}>
            <Text style={style.legendaTitulo}>Classificação:</Text>
            <View style={style.legendaItem}>
              <View style={[style.legendaColor, { backgroundColor: '#3498db' }]} />
              <Text style={style.legendaText}>Abaixo de 18.5 - Abaixo do peso</Text>
            </View>
            <View style={style.legendaItem}>
              <View style={[style.legendaColor, { backgroundColor: '#2ecc71' }]} />
              <Text style={style.legendaText}>18.5 a 24.9 - Peso normal</Text>
            </View>
            <View style={style.legendaItem}>
              <View style={[style.legendaColor, { backgroundColor: '#f39c12' }]} />
              <Text style={style.legendaText}>25 a 29.9 - Sobrepeso</Text>
            </View>
            <View style={style.legendaItem}>
              <View style={[style.legendaColor, { backgroundColor: '#e74c3c' }]} />
              <Text style={style.legendaText}>30 a 34.9 - Obesidade I</Text>
            </View>
            <View style={style.legendaItem}>
              <View style={[style.legendaColor, { backgroundColor: '#c0392b' }]} />
              <Text style={style.legendaText}>35 a 39.9 - Obesidade II</Text>
            </View>
            <View style={style.legendaItem}>
              <View style={[style.legendaColor, { backgroundColor: '#7f0000' }]} />
              <Text style={style.legendaText}>Acima de 40 - Obesidade III</Text>
            </View>
          </View>
        </Animated.View>
      )}
    </SafeAreaView>
  );
}

const style = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
    padding: 20,
  },
  header: {
    alignItems: 'center',
    marginBottom: 40,
    marginTop: 20,
  },
  titulo: {
    color: '#2c3e50',
    fontWeight: 'bold',
    fontSize: 28,
    marginBottom: 5,
    textTransform: 'uppercase',
    letterSpacing: 1,
  },
  subtitulo: {
    color: '#7f8c8d',
    fontSize: 16,
  },
  formContainer: {
    backgroundColor: '#fff',
    borderRadius: 15,
    padding: 25,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.1,
    shadowRadius: 10,
    elevation: 5,
  },
  input: {
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 10,
    padding: 15,
    marginBottom: 20,
    fontSize: 16,
    backgroundColor: '#f9f9f9',
  },
  btn: {
    backgroundColor: '#2c3e50',
    padding: 18,
    borderRadius: 10,
    alignItems: 'center',
    justifyContent: 'center',
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.2,
    shadowRadius: 5,
    elevation: 3,
  },
  btnText: {
    color: 'white',
    fontWeight: 'bold',
    fontSize: 16,
    letterSpacing: 1,
  },
  resultContainer: {
    marginTop: 30,
    backgroundColor: '#fff',
    borderRadius: 15,
    padding: 25,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.1,
    shadowRadius: 10,
    elevation: 5,
  },
  resultText: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#2c3e50',
    textAlign: 'center',
    marginBottom: 10,
  },
  classificacaoText: {
    fontSize: 20,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 20,
  },
  legendaContainer: {
    marginTop: 15,
  },
  legendaTitulo: {
    fontWeight: 'bold',
    color: '#2c3e50',
    marginBottom: 10,
  },
  legendaItem: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 8,
  },
  legendaColor: {
    width: 20,
    height: 20,
    borderRadius: 4,
    marginRight: 10,
  },
  legendaText: {
    color: '#7f8c8d',
    fontSize: 14,
  },
});
