package hanyang.likelion.kkuuk_back.model;


import hanyang.likelion.kkuuk_back.enums.PayType;
import java.time.LocalDateTime;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.ManyToOne;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.Setter;

@Entity
@Getter
@Setter
@Builder
@RequiredArgsConstructor
@AllArgsConstructor
public class History {

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  @Column(nullable = false, length = 4)
  private PayType payType;

  @ManyToOne
  private Store store;

  @ManyToOne
  private Client client;


  @Column(nullable = false)
  private LocalDateTime tradeAt;

  @Column(nullable = false)
  private Long beforeStamp;

  @Column(nullable = false)
  private Long valStamp;

  @Column(nullable = false)
  private Long afterStamp;

}


