package osori.cbhs.controller;


import io.swagger.v3.oas.annotations.Operation;

import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import org.springframework.http.ResponseEntity;
import org.springframework.http.client.HttpComponentsClientHttpRequestFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class Controller {

    @Operation(summary = "test hello", description = "hello api example")
    @ApiResponses({
            @ApiResponse(responseCode = "200", description = "OK !!"),
            @ApiResponse(responseCode = "400", description = "BAD REQUEST !!"),
            @ApiResponse(responseCode = "404", description = "NOT FOUND !!"),
            @ApiResponse(responseCode = "500", description = "INTERNAL SERVER ERROR !!")
    })
    @GetMapping("/test/")
    public ResponseEntity<String> main_page (@Parameter(description = "jwt", required = true, example = "Park") @RequestParam String jwt) {

        RestTemplate template = new RestTemplate(new HttpComponentsClientHttpRequestFactory());
        String result = template.getForObject("http://cbhs.asuscomm.com:5555/vi/info/20-2337" , String.class);
        System.out.println(result);

        return ResponseEntity.ok(result);
    }
}
