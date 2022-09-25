FROM openjdk:17
VOLUME /tmp
EXPOSE 9999
ARG JAR_FILE=build/libs/cbhs-0.0.1-SNAPSHOT.jar
ADD keystore.p12 keystore.p12
ADD ${JAR_FILE} to-do-springboot.jar
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/to-do-springboot.jar"]