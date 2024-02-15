#include <DHT.h>
#include <DHT_U.h>

// Pre-setup
  //Includes
    #include <SPI.h>
    #include <nRF24L01.h>
    #include <RF24.h>
    #include <RF24_config.h>
  // Sensor definition
    #define DHTTYPE DHT11

    #define DHT_pin 2

    
    DHT dht(DHT_pin, DHTTYPE);
    int trigPin = 8;
    int echoPin = 9;
    long duration;
    int cm = 0;
    
    float temperatura;
    float humidity;
  //Actuators definition
    //Auxiliar elements
      //Pump
        const int Pump=22; //Pump pin definition
        const int MPPump= 0; //Action (0 or 1) message position
      //Filling Valve
        const int FillingValve=23; //Pin definition
        const int MPFillingValve=2; //Action (0 or 1) message position
      //RecirculationValve
        const int RecirculationValve=24; //Pin definition
        const int MPRecirculationValve=4; //Action (0 or 1) message position
      //LeachedValve
        const int LeachedValve=25; //Pin definition
        const int MPLeachedValve=6; //Action (0 or 1) message position
    //Nutruents peristaltic pumps
      //Nutrient 1
        const int Nutrient1=26;
        const int MPNutrient1=8; //Action (0 or 1) message position
      //Nutrient 2
        const int Nutrient2=27;
        const int MPNutrient2=10; //Action (0 or 1) message position
      //Nutrient 3
        const int Nutrient3=28;
        const int MPNutrient3=12; //Action (0 or 1) message position
    //Lines  
      //L1
        const int L1=29;
        const int MPL1=14; //Action (0 or 1) message position      
      //L2
        const int L2=30;
        const int MPL2=16; //Action (0 or 1) message position  
      //L3
        const int L3=31;
        const int MPL3=18; //Action (0 or 1) message position  
      //L4
        const int L4=32;
        const int MPL4=20; //Action (0 or 1) message position  
      //L5
        const int L5=33;
        const int MPL5=22; //Action (0 or 1) message position  
      //L6
        const int L6=34;
        const int MPL6=24; //Action (0 or 1) message position        
      //L7
        const int L7=35;
        const int MPL7=26; //Action (0 or 1) message position  
      //L8
        const int L8=36;
        const int MPL8=28; //Action (0 or 1) message position  
      //Other
        const int MPMessage=30;

  //Strings definition
    String message;
    String msg;
    String bus;

    String inputString = "";      // a String to hold incoming data
    bool stringComplete = false;  // whether the string is complete

  //radio setup
    const int CE = 49;
    const int CSN = 53;

    RF24 radio (CE, CSN);

    const byte address[6] = "00001";
    float data[5];
// Setup
  void setup() {
    // Serial communication setup:
      // initialize serial:
      Serial.begin(9600);
      Serial.setTimeout(50);
      // reserve 200 bytes for the inputString:
      inputString.reserve(200);
      pinMode(DHT_pin, INPUT);
      dht.begin();
    // Radio communication setup
      radio.begin();
      radio.openReadingPipe(1,address);
      radio.startListening();
    // Digital outputs configuration  
      //Pump setup
      pinMode(Pump, OUTPUT);
      digitalWrite(Pump, HIGH);
      //FillingValve setup
      digitalWrite(FillingValve, HIGH); //action to avoid initial turnon-off due to low level trigger rele use High->rele off
      pinMode(FillingValve, OUTPUT);
      //RecirculationValve setup
      digitalWrite(RecirculationValve, HIGH); //action to avoid initial turnon-off due to low level trigger rele use High->rele off
      pinMode(RecirculationValve, OUTPUT);
      //LeachedValve setup
      digitalWrite(LeachedValve, HIGH); //action to avoid initial turnon-off due to low level trigger rele use High->rele off
      pinMode(LeachedValve, OUTPUT);
      //Nutrient1 setup
      digitalWrite(Nutrient1, HIGH); //action to avoid initial turnon-off due to low level trigger rele use High->rele off
      pinMode(Nutrient1, OUTPUT);
      //Nutrient2 setup
      digitalWrite(Nutrient2, HIGH); //action to avoid initial turnon-off due to low level trigger rele use High->rele off
      pinMode(Nutrient2, OUTPUT);
      //Nutrient3 setup
      digitalWrite(Nutrient3, HIGH); //action to avoid initial turnon-off due to low level trigger rele use High->rele off
      pinMode(Nutrient3, OUTPUT);
      //L1 setup
      digitalWrite(L1, HIGH); //action to avoid initial turnon-off due to low level trigger rele use High->rele off
      pinMode(L1, OUTPUT);
      //L2 setup
      digitalWrite(L2, HIGH); //action to avoid initial turnon-off due to low level trigger rele use High->rele off
      pinMode(L2, OUTPUT);
      //L3 setup
      digitalWrite(L3, HIGH); //action to avoid initial turnon-off due to low level trigger rele use High->rele off
      pinMode(L3, OUTPUT);
      //L4 setup
      digitalWrite(L4, HIGH); //action to avoid initial turnon-off due to low level trigger rele use High->rele off
      pinMode(L4, OUTPUT);
      //L5 setup
      digitalWrite(L5, HIGH); //action to avoid initial turnon-off due to low level trigger rele use High->rele off
      pinMode(L5, OUTPUT);
      //L6 setup
      digitalWrite(L6, HIGH); //action to avoid initial turnon-off due to low level trigger rele use High->rele off
      pinMode(L6, OUTPUT);
      //L7 setup
      digitalWrite(L7, HIGH); //action to avoid initial turnon-off due to low level trigger rele use High->rele off
      pinMode(L7, OUTPUT);
      //L8 setup
      digitalWrite(L8, HIGH); //action to avoid initial turnon-off due to low level trigger rele use High->rele off
      pinMode(L8, OUTPUT);

      pinMode(53, OUTPUT);

      //UltraSound SetUp
      pinMode(trigPin, OUTPUT);
      pinMode(echoPin, INPUT);
  }
//Loop
  void loop() {
    // put your main code here, to run repeatedly:
//           temperatura= dht.readTemperature();
//           data[0] = temperatura;
//           humidity=dht.readHumidity();
//           data[1]=humidity;
           int cm = ping(trigPin, echoPin);
           data[3] = cm;
            Serial.println(String(cm));
//           Serial.print(temperatura);
//           Serial.print("\n");
//           Serial.print(humidity);
//           Serial.print("\n");
//           Serial.print(cm);
//           Serial.print("\n");
           delay(50);

    if(Serial.available()>0){
      //msg=inputString;
       msg=Serial.readStringUntil('\n');
      String DFSt= msg.substring(MPMessage,MPMessage+1);
      if (DFSt=="D"){

        //Serial.println("1,2,3,4");
        //Serial.println(String(data[0])+","+String(data[1])+","+String(data[2])+","+String(data[3])+","+String(data[4]));
        Serial.println(String(cm));
      }
      //DataFunction();
      PumpFunction();
      FillingValveFunction();
      RecirculationValveFunction();
      LeachedValveFunction();
      Nutrient1Function();
      Nutrient2Function();
      Nutrient3Function();
      L1Function();
      L2Function();
      L3Function();
      L4Function();
      L5Function();
      L6Function();
      L7Function();
      L8Function();
    }
  }
//Serial Event
  /*
    SerialEvent occurs whenever a new data comes in the hardware serial RX. This
    routine is run between each time loop() runs, so using delay inside loop can
    delay response. Multiple bytes of data may be available.
  */
//  void serialEvent() {
//    while (Serial.available()) {
//      // get the new byte:
//      char inChar = (char)Serial.read();
//      // add it to the inputString:
//      inputString += inChar;
//      // if the incoming character is a newline, set a flag so the main loop can
//      // do something about it:
//      if (inChar == '\n') {
//        stringComplete = true;
//      }
//    }
//  }

// Functions definition
  void PumpFunction(){
        // Pump action 
        String PumpSt= msg.substring(MPPump,MPPump+1);
        if (PumpSt=="0"){
          digitalWrite(Pump, HIGH);
          } else if (PumpSt=="1"){
          digitalWrite(Pump, LOW);
        }
  }

  void FillingValveFunction(){
        // FillingValve action 
        String FillingValveSt= msg.substring(MPFillingValve,MPFillingValve+1);
        if (FillingValveSt=="1"){
          digitalWrite(FillingValve, LOW);
          } else if (FillingValveSt=="0"){
          digitalWrite(FillingValve, HIGH);
        }
  }

  void RecirculationValveFunction(){
        // RecirculationValve action 
        String RecirculationValveSt= msg.substring(MPRecirculationValve,MPRecirculationValve+1);
        if (RecirculationValveSt=="1"){
          digitalWrite(RecirculationValve, LOW);
          } else if (RecirculationValveSt=="0"){
          digitalWrite(RecirculationValve, HIGH);
        }
  }

  void LeachedValveFunction(){ // MODIFICAR SERA RELE
        // LeachedValve action 
        String LeachedValveSt= msg.substring(MPLeachedValve,MPLeachedValve+1);
        if (LeachedValveSt=="1"){
          digitalWrite(LeachedValve, LOW);
          } else if (LeachedValveSt=="0"){
          digitalWrite(LeachedValve, HIGH);
        }
  }

  void Nutrient1Function(){
        // Nutrient1 action 
        String Nutrient1St= msg.substring(MPNutrient1,MPNutrient1+1);
        if (Nutrient1St=="1"){
          digitalWrite(Nutrient1, LOW);
          } else if (Nutrient1St=="0"){
          digitalWrite(Nutrient1, HIGH);
        }
  }

  void Nutrient2Function(){
        // Nutrient2 action 
        String Nutrient2St= msg.substring(MPNutrient2,MPNutrient2+1);
        if (Nutrient2St=="1"){
          digitalWrite(Nutrient2, LOW);
          } else if (Nutrient2St=="0"){
          digitalWrite(Nutrient2, HIGH);
        }
  }

  void Nutrient3Function(){
        // Nutrient3 action 
        String Nutrient3St= msg.substring(MPNutrient3,MPNutrient3+1);
        if (Nutrient3St=="1"){
          digitalWrite(Nutrient3, LOW);
          } else if (Nutrient3St=="0"){
          digitalWrite(Nutrient3, HIGH);
        }
  }

  void L1Function(){
        // L1 action 
        String L1St= msg.substring(MPL1,MPL1+1);
        if (L1St=="1"){
          digitalWrite(L1, LOW);
          } else if (L1St=="0"){
          digitalWrite(L1, HIGH);
        }
  }

  void L2Function(){
        // L2 action 
        String L2St= msg.substring(MPL2,MPL2+1);
        if (L2St=="1"){
          digitalWrite(L2, LOW);
          } else if (L2St=="0"){
          digitalWrite(L2, HIGH);
        }
  }

  void L3Function(){
        // L3 action 
        String L3St= msg.substring(MPL3,MPL3+1);
        if (L3St=="1"){
          digitalWrite(L3, LOW);
          } else if (L3St=="0"){
          digitalWrite(L3, HIGH);
        }
  }

  void L4Function(){
        // L4 action 
        String L4St= msg.substring(MPL4,MPL4+1);
        if (L4St=="1"){
          digitalWrite(L4, LOW);
          } else if (L4St=="0"){
          digitalWrite(L4, HIGH);
        }
  }

  void L5Function(){
        // L5 action 
        String L5St= msg.substring(MPL5,MPL5+1);
        if (L5St=="1"){
          digitalWrite(L5, LOW);
          } else if (L5St=="0"){
          digitalWrite(L5, HIGH);
        }
  }

  void L6Function(){
        // L6 action 
        String L6St= msg.substring(MPL6,MPL6+1);
        if (L6St=="1"){
          digitalWrite(L6, LOW);
          } else if (L6St=="0"){
          digitalWrite(L6, HIGH);
        }
  }

  void L7Function(){
        // L7 action 
        String L7St= msg.substring(MPL7,MPL7+1);
        if (L7St=="1"){
          digitalWrite(L7, LOW);
          } else if (L7St=="0"){
          digitalWrite(L7, HIGH);
        }
  }

  void L8Function(){
        // L8 action 
        String L8St= msg.substring(MPL8,MPL8+1);
        if (L8St=="1"){
          digitalWrite(L8, LOW);
          } else if (L8St=="0"){
          digitalWrite(L8, HIGH);
        }
  }
  int ping(int TriggerPin, int EchoPin) {
    long duration, distanceCm;
  
    digitalWrite(TriggerPin, LOW);  //para generar un pulso limpio ponemos a LOW 4us
    delayMicroseconds(4);
    digitalWrite(TriggerPin, HIGH);  //generamos Trigger (disparo) de 10us
    delayMicroseconds(10);
    digitalWrite(TriggerPin, LOW);
  
    duration = pulseIn(EchoPin, HIGH);  //medimos el tiempo entre pulsos, en microsegundos
  
    distanceCm = duration * 0.034 / 2;   //convertimos a distancia, en cm
    return distanceCm;
}


//*****Peaces*****//
//void DataFunction(){
      // L4 action
//      String DFSt= msg.substring(18,19); 
//      if (DFSt=="D"){
//        Serial.println("1,2,3,4");
//      }
//}
