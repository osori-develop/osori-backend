package osori.cbhs.controller;

import io.swagger.v3.oas.annotations.Operation;
import osori.cbhs.controller.dto.MemberInfoDto;
import osori.cbhs.controller.dto.MemberResponseDto;
import osori.cbhs.service.MemberService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequiredArgsConstructor
@RequestMapping("/member")
public class MemberController {
    private final MemberService memberService;


    @Operation(summary = "유저정보", description = "토큰을 활용하여 유저 정보 가져오기")
    @GetMapping("/me")
    public ResponseEntity<MemberInfoDto> getMyMemberInfo() {
        return ResponseEntity.ok(memberService.getMyInfo());
    }


//    @GetMapping("/{email}")
//    public ResponseEntity<MemberResponseDto> getMemberInfo(@PathVariable String email) {
//        return ResponseEntity.ok(memberService.getMemberInfo(email));
//    }
}