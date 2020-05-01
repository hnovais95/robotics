#include <iostream>
#include <cmath>

using namespace std;

/* Este programa calcula os ângulos das junções de um manipulador de
   dois graus de liberdade em movimento plano.

   Autor: Heitor Novais

   */

int main()
{
    double a1=1; //Comprimento do elo 1
    double a2=1; //Comprimento do elo 2
    double x;  //Coordenada X do plano cartesiano
    double y;  //Coordenada Y do plano cartesiano
    double o1; //Ângulo formado pela junta 1 a partir da base
    double o2; //Ângulo formado pela junta 2 a partir da base
    double pi = 3.141592265359;
    int flag = 0;

    do
    {
        cout << "Insira a coordenada X da posicao do ponto terminal no plano XY: ";
        cin >> x;
        cout << "Insira a coordenada Y da posicao do ponto terminal no plano XY: ";
        cin >> y;

        /* A partir da trigonometria obtemos:

        x = a1*cos(o1) + a2*cos(o1+o2)
        y = a1*sin(o1) + a2*sin(o1+o2)

        Aplicando regra do paralelograma tem-se:

        x^2 + y^2 = a1^2 + a2^2 + 2*a1*a2*cos(o2)

        Que implica:

        cos(o2) = (x^2 + y^2 - a1^2 - a2^2)/(2*a1*a2) */

        o2 = abs(acos((pow(x,2) + pow(y,2) - pow(a1,2) - pow(a2,2))/(2*a1*a2))); //Considerando o2>0 -> Cotovelo pra cima

        /* A partir de manipulações trigonométricas temos que: */

        o1 = atan((y*(a1+a2*cos(o2))-x*a2*sin(o2))/(x*(a1+a2*cos(o2)+y*a2*sin(o2))));

        cout << "\nOs angulos formados pelas juntas sao o1 = " << 180*o1/pi << " e o2 = " << 180*o2/pi <<endl;

        cout << "\nDeseja calcular novamente? (1 - sim)" << endl;
        cin >> flag;

    } while (flag == 1);

    return 0;
}
