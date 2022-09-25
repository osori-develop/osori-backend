package osori.cbhs.controller;

import io.swagger.v3.oas.annotations.Operation;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;
import osori.cbhs.entity.Cbhs2_menu;
import osori.cbhs.repository.Cbhs2_menuReposifory;

import java.util.Date;
import java.util.Optional;

@RestController
@RequiredArgsConstructor
@RequestMapping("/menu")
public class MenuController {

    private final Cbhs2_menuReposifory cbhs2_menuReposifory;

    @Operation(summary = "메뉴가져오기", description = "토큰을 활용하여 유저 정보 가져오기")
    @GetMapping("/cbhs2/")
    public Optional<Cbhs2_menu> get_cbhs2_menu() {

        return cbhs2_menuReposifory.findById(2L);
                //cbhs2_menuReposifory.findByDate(new Date("2022-08-20"));

    }


}