#include <iostream>
#include <cmath>

float potega_f(int k){
    float pom=10;
    for (int i=0;i<k;i++){
        pom/=10;
    }
    return pom;
}

double potega_d(int k){
    double pom=10;
    for (int i=0;i<k;i++){
        pom/=10;
    }
    return pom;
}

long double potega_ld(int k){
    long double pom=10;
    for (int i=0;i<k;i++){
        pom/=10;
    }
    return pom;
}

float rownanie1_float(int k){
    float pom = potega_f(k);
    return float((pow(exp(1),pom)-1)/pom);
}

float rownanie2_float(int k){
    float pom = potega_f(k);
    return float((pow(exp(1),pom)-1)/log(exp(pom)));
}

double rownanie1_double(int k){
    double pom = potega_d(k);
    return (pow(exp(1),pom)-1)/pom;
}

double rownanie2_double(int k){
    double pom = potega_d(k);
    return (pow(exp(1),pom)-1)/log(exp(pom));
}

long double rownanie1_long_double(int k){
    long double pom = potega_ld(k);
    return (long double)((pow(exp(1),pom)-1)/pom);
}

long double rownanie2_long_double(int k){
    long double pom = potega_ld(k);
    return (long double)((pow(exp(1),pom)-1)/log(exp(pom)));
}

int main() {
    std::cout.precision(10000);

    std::cout<<"float, rownanie 1\n";
    for (int k=1;k<=15;k++){
        std::cout<<"k="<<k<<":\t"<<rownanie1_float(k)<<"\n";
    }
    std::cout<<"\ndouble, rownanie 1\n";
    for (int k=1;k<=15;k++){
        std::cout<<" k="<<k<<":\t"<<rownanie1_double(k)<<"\n";
    }

    std::cout<<"\nlong double, rownanie 1\n";
    for (int k=1;k<=15;k++){
        std::cout<<"k="<<k<<":\t"<<rownanie1_long_double(k)<<"\n";
    }

    std::cout<<"\nfloat, rownanie 2\n";
    for (int k=1;k<=15;k++){
        std::cout<<"k="<<k<<":\t"<<rownanie2_float(k)<<"\n";
    }
    std::cout<<"\ndouble, rownanie 2\n";
    for (int k=1;k<=15;k++){
        std::cout<<" k="<<k<<":\t"<<rownanie2_double(k)<<"\n";
    }

    std::cout<<"\nlong double, rownanie 2\n";
    for (int k=1;k<=15;k++){
        std::cout<<"k="<<k<<":\t"<<rownanie2_long_double(k)<<"\n";
    }
    return 0;
}



/*float e=2.71828182845904523536028747135266249775724709369995;
double e2=2.71828182845904523536028747135266249775724709369995;
long double e3=2.71828182845904523536028747135266249775724709369995;
std::cout.precision(10000);
std::cout<<"float e:\t"<<e<<"\ndouble e:\t"<<e2<<"\nlong double e:\t"<<e3<<"\nexp(1):\t\t"<<exp(1)<<"\n";*/