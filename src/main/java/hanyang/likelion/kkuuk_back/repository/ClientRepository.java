package hanyang.likelion.kkuuk_back.repository;

import hanyang.likelion.kkuuk_back.model.Client;
import hanyang.likelion.kkuuk_back.model.Store;
import java.util.List;
import java.util.Optional;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ClientRepository extends JpaRepository<Client,Long> {

  public Optional<Client> findByNameAndLast4Digit(String name, String last4digit);

  public List<Client> findAllByNameAndStore(String name, Store store);

  public List<Client> findAllByLast4DigitAndStore(String last4digit, Store store);
}
