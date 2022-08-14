package osori.cbhs.controller;



import io.swagger.v3.oas.annotations.Operation;
import osori.cbhs.controller.dto.MemberRequestDto;
import osori.cbhs.controller.dto.MemberResponseDto;
import osori.cbhs.controller.dto.TokenRequestDto;
import osori.cbhs.controller.dto.TokenDto;
import osori.cbhs.service.AuthService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/auth")
@RequiredArgsConstructor
public class AuthController {
    private final AuthService authService;


    @Operation(summary = "어플 로그인 및 가입", description = "학사번호와 학사비밀번호를 입력 -> 학사회원존재 하나 디비에 등록 안되있으면 디비 등록후 토큰 반환, 디비 등록되어있으면 그냥 토큰반환")
    @PostMapping("/signup")
    public ResponseEntity<TokenDto> signup(@RequestBody MemberRequestDto memberRequestDto) {
        return ResponseEntity.ok(authService.signup(memberRequestDto));
    }

//    @PostMapping("/login")
//    public ResponseEntity<TokenDto> login(@RequestBody MemberRequestDto memberRequestDto) {
//        return ResponseEntity.ok(authService.login(memberRequestDto));
//    }

    @Operation(summary = "토큰 재발급", description = "토큰 입력시 토큰 재발급")
    @PostMapping("/reissue")
    public ResponseEntity<TokenDto> reissue(@RequestBody TokenRequestDto tokenRequestDto) {
        return ResponseEntity.ok(authService.reissue(tokenRequestDto));
    }
}
