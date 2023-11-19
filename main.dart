import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Soamer Payback'),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Spacer(),
          // Foto Grande
          Container(
            width: 375,
            height: 200,
            decoration: BoxDecoration(
              image: DecorationImage(
                alignment: Alignment.center,
                image: AssetImage('assets/grafico.png'),
                fit: BoxFit.cover,
              ),
            ),
          ),

          // Espaçamento entre a foto e os botões
          SizedBox(height: 20),
          Spacer(),

          // Botões
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              IconButton(
                onPressed: () {
                  Navigator.push(context, MaterialPageRoute(builder: (context) => LivroMenuPage()));
                },
                icon: Icon(Icons.menu_book_sharp),
              ),
              IconButton(
                onPressed: () {
                  // Lógica para o segundo botão
                },
                icon: Icon(Icons.attach_money),
              ),
              IconButton(
                onPressed: () {
                  // Lógica para o terceiro botão
                },
                icon: Icon(Icons.settings),
              ),
            ],
          ),
        ],
      ),
    );
  }
}

class LivroMenuPage extends StatelessWidget {
  final List<String> concessionarias = ['Fiat Barigui', 'Chevrolet Metrosul', 'Hyundai HMB'];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Concessionárias'),
      ),
      body: ListView.builder(
        itemCount: concessionarias.length,
        itemBuilder: (context, index) {
          return ListTile(
            title: Text(concessionarias[index]),
            onTap: () {
              // Lógica ao clicar na concessionária
              _handleConcessionariaClick(context, concessionarias[index]);
            },
          );
        },
      ),
      bottomNavigationBar: _buildFinalizarButton(context),
    );
  }

  Widget _buildFinalizarButton(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: EdgeInsets.all(16.0),
      child: IconButton(
        onPressed: () {
          // Lógica ao clicar no botão "Finalizar"
          _handleFinalizarClick(context);
        },
        icon: Icon(Icons.add),
      ),
    );
  }

  void _handleConcessionariaClick(BuildContext context, String concessionaria) {
    // Implemente a lógica específica para cada concessionária
    // Neste exemplo, abrimos a página de vendedores para cada concessionária
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => VendedoresPage(concessionaria: concessionaria)),
    );
  }

  void _handleFinalizarClick(BuildContext context) {
    // Lógica ao clicar no botão "Finalizar"
    print('Finalizar clicado na LivroMenuPage');
    // Adicione aqui qualquer ação que deseja realizar ao clicar no botão "Finalizar"
  }
}

class VendedoresPage extends StatelessWidget {
  final String concessionaria;
  final List<String> vendedores;

  VendedoresPage({required this.concessionaria}) : vendedores = _getVendedores(concessionaria);

  static List<String> _getVendedores(String concessionaria) {
    // Lógica para obter a lista de vendedores com base na concessionária
    // Este é um exemplo simples, você pode substituir com a lógica real
    if (concessionaria == 'Fiat Barigui') {
      return ['Davi Coene', 'Camila Fideli'];
    } else if (concessionaria == 'Chevrolet Metrosul') {
      return ['Gustavo Debatin', 'João Victor Soares'];
    } else if (concessionaria == 'Hyundai HMB') {
      return ['Lucas Baleiro', 'Queli Terezinha'];
    } else {
      return [];
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Vendedores - $concessionaria'),
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: vendedores.length,
              itemBuilder: (context, index) {
                return ListTile(
                  title: Text(vendedores[index]),
                  onTap: () {
                    // Lógica ao clicar no vendedor
                    _handleVendedorClick(context, vendedores[index]);
                  },
                );
              },
            ),
          ),
          _buildFinalizarButton(context),
        ],
      ),
    );
  }

  Widget _buildFinalizarButton(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: EdgeInsets.all(16.0),
      child: IconButton(
                onPressed: () {
                  // Lógica para o terceiro botão
                },
                icon: Icon(Icons.add),
              ),
    );
  }

  void _handleVendedorClick(BuildContext context, String vendedor) {
    // Implemente a lógica específica para cada vendedor
    // Neste exemplo, abrimos a página de detalhes do vendedor para cada vendedor
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => DetalhesVendedorInfoPage(vendedor: vendedor)),
    );
  }

  void _handleFinalizarClick(BuildContext context) {
    // Lógica ao clicar no botão "Finalizar"
    print('Finalizar clicado');
    // Adicione aqui qualquer ação que deseja realizar ao clicar no botão "Finalizar"
  }
}

class DetalhesVendedorInfoPage extends StatelessWidget {
  final String vendedor;

  DetalhesVendedorInfoPage({required this.vendedor});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Detalhes do Vendedor - $vendedor'),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        children: [
          _buildDetalhe('Nome completo', vendedor),
          _buildDetalhe('CPF', '123.456.789-00'), // Substitua pelo CPF real
          _buildDetalhe('Número de telefone', '123456789'), // Substitua pelo telefone real
          _buildDetalhe('Email', '$vendedor@example.com'), // Substitua pelo email real
        ],
      ),
    );
  }

  Widget _buildDetalhe(String label, String value) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(label),
          Text(value),
        ],
      ),
    );
  }
}