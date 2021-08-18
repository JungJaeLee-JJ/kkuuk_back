package hanyang.likelion.kkuuk_back.repository;

import hanyang.likelion.kkuuk_back.model.Store;
import java.util.Optional;
import org.apache.catalina.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface StoreRepository extends JpaRepository<Store,Long> {
  Boolean existsByUsername(String username);
  Optional<Store> findByUsername(String username);
}
