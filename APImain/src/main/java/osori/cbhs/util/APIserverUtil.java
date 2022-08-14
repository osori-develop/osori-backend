package osori.cbhs.util;

import com.fasterxml.jackson.databind.util.JSONPObject;
import lombok.Data;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseCookie;
import org.springframework.http.ResponseEntity;
import org.springframework.http.converter.HttpMessageConverter;
import org.springframework.stereotype.Component;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;
import osori.cbhs.controller.dto.MemberInfoDto;

import java.util.ArrayList;
import java.util.List;

@Component
@Data
public class APIserverUtil {

    @Value("${parser.url}")
    private String url;

    @Value("${parser.port}")
    private String port;


    public boolean Getexist (String id, String pw) {

        String get_url = "http://" + url + ":" + port + "/v1/exist/" + id + "/" + pw ;

        // RestTemplate 에 MessageConverter 세팅
        List<HttpMessageConverter<?>> converters = new ArrayList<HttpMessageConverter<?>>();
        //converters.add(new FormHttpMessageConverter());
        //converters.add(new StringHttpMessageConverter());

        RestTemplate restTemplate = new RestTemplate();
        //restTemplate.setMessageConverters(converters);

        // parameter 세팅
        //MultiValueMap<String, String> map = new LinkedMultiValueMap<String, String>();
        //map.add("str", "thisistest");

        // REST API 호출
        String result = restTemplate.getForObject(get_url,  String.class);

        if (result.trim().equals("1") ) {
            System.out.println("ture");
            return true;
        }

        else  {
            System.out.println("false");
            return false;
        }

    }


    public MemberInfoDto GetInfo(String id) {

        String get_url = "http://" + url + ":" + port + "/v1/info/" + id  ;



        List<HttpMessageConverter<?>> converters = new ArrayList<HttpMessageConverter<?>>();
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<MemberInfoDto> result = restTemplate.getForEntity(get_url,MemberInfoDto.class);
        return result.getBody();

    }

}
