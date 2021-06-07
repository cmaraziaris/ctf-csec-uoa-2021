#pragma once

#include <stdio.h>

int Base64Decode(char* b64message, unsigned char** buffer, size_t* length);
void Base64DecodeStr(char* b64message, char* dest, int n);