#!/usr/bin/env python
import rospy
import RPi.GPIO as GPIO
#import time
from sensor_msgs.msg import JointState

#------------------------------------------------------------------------------
#configurando GPIO's
#------------------------------------------------------------------------------
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

servo_1_Pin = 40
servo_2_Pin = 37
servo_3_Pin = 38
servo_4_Pin = 36
servo_5_Pin = 35
servo_6_Pin = 33

GPIO.setup(servo_1_Pin,GPIO.OUT)
GPIO.setup(servo_2_Pin,GPIO.OUT)
GPIO.setup(servo_3_Pin,GPIO.OUT)
GPIO.setup(servo_4_Pin,GPIO.OUT)
GPIO.setup(servo_5_Pin,GPIO.OUT)
GPIO.setup(servo_6_Pin,GPIO.OUT)

pwm_1=GPIO.PWM(servo_1_Pin,50)
pwm_2=GPIO.PWM(servo_2_Pin,50)
pwm_3=GPIO.PWM(servo_3_Pin,50)
pwm_4=GPIO.PWM(servo_4_Pin,50)
pwm_5=GPIO.PWM(servo_5_Pin,50)
pwm_6=GPIO.PWM(servo_6_Pin,50)

pwm_1.start(0)
pwm_2.start(0)
pwm_3.start(0)
pwm_4.start(0)
pwm_5.start(0)
pwm_6.start(0)

#------------------------------------------------------------------------------
#metodos globais
#------------------------------------------------------------------------------
def rad_para_grau(junta, angulo_rad):
    if junta == 2:
        angulo_rad = angulo_rad + 2.04
        return angulo_rad * 180 / 3.142
    elif junta == 3:
        print('rad_para_gray:' + str(angulo_rad))
        angulo_rad = angulo_rad + 1.57
        return angulo_rad * 180 / 3.142
    elif junta == 5:
        angulo_rad = angulo_rad - 2.36
        return angulo_rad * 180 / 3.142
    else:
        return angulo_rad * 180 / 3.142

def calcular_limites(junta, angulo):
    if junta == 1 or junta == 2 or junta == 6:
        if angulo < 1:
            return 0
        if angulo > 180:
            return 180
    elif junta == 3:
        print('calcular_limites:' + str(angulo))
        if angulo < 15:
            return 15
        if angulo > 180:
            return 180
    elif junta == 4:
        if angulo < 10:
            return 10
        if angulo > 180:
            return 180
    elif junta == 5:
        if angulo < 1:
            return 0
        if angulo > 170:
            return 170
    #se nao angulo nao for menor ou maior que os limites, retorna o proprio
    #angulo
    return angulo

def programa(pos):
    #imprime posicoes
    print(pos)
    #converte angulo recebido por mensagem para graus, dentro dos limites
    #estabelicidos
    angulo_desejado_1 = rad_para_grau(1,  pos[0])
    angulo_desejado_1 = calcular_limites(1, angulo_desejado_1)
    
    angulo_desejado_2 = rad_para_grau(2,  pos[1])
    angulo_desejado_2 = calcular_limites(2, angulo_desejado_2)
    
    angulo_desejado_3 = rad_para_grau(3,  pos[2])
    angulo_desejado_3 = calcular_limites(3, angulo_desejado_3)
    print('Junta 3: ' + str(angulo_desejado_3))
    
    angulo_desejado_4 = rad_para_grau(4,  pos[3])
    angulo_desejado_4 = calcular_limites(4, angulo_desejado_4)
    
    angulo_desejado_5 = rad_para_grau(5,  pos[4])
    angulo_desejado_5 = calcular_limites(5, angulo_desejado_5)
    
    angulo_desejado_6 = rad_para_grau(6,  pos[5])
    angulo_desejado_6 = calcular_limites(6, angulo_desejado_6)
    
    DC_1 = 1./18.*(angulo_desejado_1)+2
    pwm_1.ChangeDutyCycle(DC_1)
    #time.sleep(0.5)
    
    DC_2 = 1./18.*(angulo_desejado_2)+2
    pwm_2.ChangeDutyCycle(DC_2)
    #time.sleep(0.5)
    
    DC_3 = 1./18.*(angulo_desejado_3)+2
    pwm_3.ChangeDutyCycle(DC_3)
    #time.sleep(0.5)
    
    DC_4 = 1./18.*(angulo_desejado_4)+2
    pwm_4.ChangeDutyCycle(DC_4)
    #time.sleep(0.5)
    
    DC_5 = 1./18.*(angulo_desejado_5)+2
    pwm_5.ChangeDutyCycle(DC_5)
    #time.sleep(0.5)
    
    DC_6 = 1./18.*(angulo_desejado_6)+2
    pwm_6.ChangeDutyCycle(DC_6)
    #time.sleep(0.5)

def callback(msg):
    programa(msg.position)
    
#------------------------------------------------------------------------------
#'main'
#------------------------------------------------------------------------------
rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('joint_states', JointState, callback)
rospy.spin()

#------------------------------------------------------------------------------
#desabilita GPIO's ao finalizar script
#------------------------------------------------------------------------------
pwm_1.stop()
pwm_2.stop()
pwm_3.stop()
pwm_4.stop()
pwm_5.stop()
pwm_6.stop()
GPIO.cleanup()