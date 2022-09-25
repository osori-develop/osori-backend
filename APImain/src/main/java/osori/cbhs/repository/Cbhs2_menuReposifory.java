package osori.cbhs.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import osori.cbhs.entity.Cbhs2_menu;
import osori.cbhs.entity.Member;

import java.util.Date;
import java.util.Optional;

@Repository
public interface Cbhs2_menuReposifory extends  JpaRepository<Cbhs2_menu,Long>{
    //Optional<Cbhs2_menu> findByDate(Date day);
}





