package osori.cbhs.controller.dto;

import osori.cbhs.entity.Authority;
import osori.cbhs.entity.Member;
import lombok.*;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.password.PasswordEncoder;

@Getter
@AllArgsConstructor
@NoArgsConstructor
public class MemberRequestDto {

    private String email;
    private String password;

    public Member toMember(PasswordEncoder passwordEncoder, MemberInfoDto infoDto) {
        return Member.builder()
                .email(email)
                .password(passwordEncoder.encode(password))
                .authority(Authority.ROLE_USER)
                .name(infoDto.getName())
                .floor(infoDto.getFloor())
                .room(infoDto.getRoom())
                .room_num(infoDto.getRoom_num())
                .date(infoDto.getDate())
                .build();
    }

    public UsernamePasswordAuthenticationToken toAuthentication() {
        return new UsernamePasswordAuthenticationToken(email, password);
    }
}
