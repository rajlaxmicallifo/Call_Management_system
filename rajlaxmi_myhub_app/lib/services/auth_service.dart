import 'dart:convert';
import 'package:http/http.dart' as http;

class AuthService {
  static const String baseUrl = 'https://call-management-backend-mnoylfu0b.vercel.app';
  String? authToken;

  // =======================
  // Test Connection
  // =======================
  Future<void> testConnection() async {
    print('🚀 Testing backend connection...');

    try {
      // Test health endpoint
      final healthResponse = await http.get(Uri.parse('$baseUrl/health/'));
      print('✅ Health check: ${healthResponse.statusCode} - ${healthResponse.body}');

      // Test accounts API endpoint
      final accountsResponse = await http.get(Uri.parse('$baseUrl/api/accounts/'));
      print('✅ Accounts API: ${accountsResponse.statusCode} - ${accountsResponse.body}');

      // Test calls API endpoint
      final callsResponse = await http.get(Uri.parse('$baseUrl/api/calls/'));
      print('✅ Calls API: ${callsResponse.statusCode} - ${callsResponse.body}');

    } catch (e) {
      print('❌ Connection test failed: $e');
    }
  }

  // =======================
  // Register User
  // =======================
  Future<String> register(String name, String email, String password) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/api/accounts/register/'),
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({
          'username': email,
          'email': email,
          'password': password,
          'name': name,
        }),
      );

      print('📡 Register Response: ${response.statusCode} - ${response.body}');

      if (response.statusCode == 201 || response.statusCode == 200) {
        final data = jsonDecode(response.body);
        authToken = data['token'] ?? data['access'] ?? data['key'];
        return "Registration successful";
      } else {
        return "Error: ${response.body}";
      }
    } catch (e) {
      return "Network error: $e";
    }
  }

  // =======================
  // Login User
  // =======================
  Future<String> login(String email, String password) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/api/accounts/login/'),
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({
          'username': email,
          'password': password,
        }),
      );

      print('📡 Login Response: ${response.statusCode} - ${response.body}');

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        authToken = data['token'] ?? data['access'] ?? data['key'];
        return "Login successful";
      } else {
        return "Invalid credentials: ${response.body}";
      }
    } catch (e) {
      return "Network error: $e";
    }
  }

  // =======================
  // Logout User
  // =======================
  Future<void> logout() async {
    authToken = null;
    print('✅ User logged out');
  }

  // =======================
  // Check if user is logged in
  // =======================
  bool isLoggedIn() {
    return authToken != null;
  }
}