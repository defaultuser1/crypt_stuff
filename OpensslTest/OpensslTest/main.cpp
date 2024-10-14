#include <string>
#include <fstream>

#include <openssl/ssl.h>

#include <iostream>
#include <vector>
#include <locale>
#include <windows.h>


int main(int argc, char** argv) {
    // Initializing OpenSLL
    const EVP_CIPHER* cipher;
    const EVP_MD* dgst = NULL;
    unsigned char key[EVP_MAX_KEY_LENGTH], iv[EVP_MAX_IV_LENGTH];

    // Setting password

    const char* password = "test";
    const unsigned char* salt = (const unsigned char*)"AAAAAAAA";
    int i;

    OpenSSL_add_all_algorithms();


    // Getting key and iv

    cipher = EVP_get_cipherbyname("aes-256-cbc");
    if (!cipher) { fprintf(stderr, "no such cipher\n"); return 1; }

    dgst = EVP_get_digestbyname("sha1");
    if (!dgst) { fprintf(stderr, "no such digest\n"); return 1; }

    if (!EVP_BytesToKey(cipher, dgst, salt,
        (unsigned char*)password,
        strlen(password), atoi(argv[1]), key, iv))
    {
        fprintf(stderr, "EVP_BytesToKey failed\n");
        return 1;
    }


    // Output key and iv to the screen

    printf("Key: "); for (i = 0; i < 32; ++i) { printf("%02x", key[i]); } printf("\n");
    printf("IV: "); for (i = 0; i < 16; ++i) { printf("%02x", iv[i]); } printf("\n");
}