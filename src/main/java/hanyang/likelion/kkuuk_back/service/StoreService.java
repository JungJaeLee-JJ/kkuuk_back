package hanyang.likelion.kkuuk_back.service;

import hanyang.likelion.kkuuk_back.exception.CustomException;
import hanyang.likelion.kkuuk_back.exception.ExceptionEnum;
import hanyang.likelion.kkuuk_back.model.Client;
import hanyang.likelion.kkuuk_back.model.Store;
import hanyang.likelion.kkuuk_back.payload.ClientResponseForm;
import hanyang.likelion.kkuuk_back.payload.ClientsByLast4DigitRequestForm;
import hanyang.likelion.kkuuk_back.payload.ClientsByUsernameRequestForm;
import hanyang.likelion.kkuuk_back.payload.DuplicateRequestForm;
import hanyang.likelion.kkuuk_back.payload.DuplicateResponseForm;
import hanyang.likelion.kkuuk_back.payload.EnrollClientRequestForm;
import hanyang.likelion.kkuuk_back.payload.EnrollClientResponseForm;
import hanyang.likelion.kkuuk_back.payload.LoginRequestForm;
import hanyang.likelion.kkuuk_back.payload.LoginResponseForm;
import hanyang.likelion.kkuuk_back.payload.ResponseForm;
import hanyang.likelion.kkuuk_back.payload.SignUpRequestForm;
import hanyang.likelion.kkuuk_back.payload.SignUpResponseForm;
import hanyang.likelion.kkuuk_back.payload.StampRequestForm;
import hanyang.likelion.kkuuk_back.payload.StoreInfo;
import hanyang.likelion.kkuuk_back.repository.ClientRepository;
import hanyang.likelion.kkuuk_back.repository.StoreRepository;
import hanyang.likelion.kkuuk_back.util.JwtTokenProvider;
import java.time.LocalDateTime;
import java.util.Collections;
import java.util.List;
import java.util.Optional;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestBody;

@Slf4j
@Service
@RequiredArgsConstructor
public class StoreService {

  private final StoreRepository storeRepository;

  private final ClientRepository clientRepository;

  private final JwtTokenProvider jwtTokenProvider;
  private final PasswordEncoder passwordEncoder;

  public SignUpResponseForm signUp(SignUpRequestForm form){
    Store store =  storeRepository.save(Store.builder()
        .username(form.getEmail())
        .password(passwordEncoder.encode(form.getPassword()))
        .call(form.getCall())
        .roles(Collections.singletonList("ROLE_USER"))
        .name(form.getName())
        .createAt(LocalDateTime.now())
        .build());

    return SignUpResponseForm.of("가맹점 등록을 완료하였습니다.", store);
  }

  public DuplicateResponseForm DuplicateCheck(DuplicateRequestForm form){
    Boolean ret = storeRepository.existsByUsername(form.getEmail());
    if (!ret) {
      return new DuplicateResponseForm("사용가능한 email 입니다.",Boolean.FALSE);
    }
    return new DuplicateResponseForm("중복된 email 입니다.",Boolean.TRUE);
  }

  public LoginResponseForm login(LoginRequestForm loginRequestForm) {
    Store store = storeRepository.findByUsername(loginRequestForm.getEmail()).orElseThrow(() ->
        new IllegalArgumentException(loginRequestForm.getEmail())
    );
//    if (!passwordEncoder.matches(store.getPassword(), loginRequestForm.getPassword())) {
//      return new LoginResponseForm("로그인에 실패하였습니다.", store,"");
//    }
    return new LoginResponseForm("로그인에 성공하였습니다.", store,jwtTokenProvider.createToken(store.getUsername(), store.getAuthorities()));
  }

  public StoreInfo getInfo(String token) {
    Store store = null;
    StoreInfo res = null;
    try{
      String email = jwtTokenProvider.getUserPk(token);
      store = storeRepository.findByUsername(email).get();
      res = StoreInfo.of(store);
    } catch (Exception e){
      throw CustomException.of(ExceptionEnum.BAD_REQUEST, "사용자 정보를 찾을 수 없습니다.");
    }
    return res;
  }

  public EnrollClientResponseForm enrollClient(EnrollClientRequestForm form) {
    Store store = storeRepository.findById(form.getStoreId()).get();
    Client client = clientRepository.save(Client.builder()
        .store(store)
        .last4Digit(form.getLast4digit())
        .name(form.getUsername())
        .createAt(LocalDateTime.now())
        .stamp(0L)
        .build());
    return new EnrollClientResponseForm("고객 등록을 완료하였습니다.", client);
  }

  public ClientResponseForm clientByDigit(ClientsByLast4DigitRequestForm form){
    Store store = storeRepository.findById(form.getStoreId()).get();
    List<Client> clientList = clientRepository.findAllByLast4DigitAndStore(form.getLast4digit(),store);
    return ClientResponseForm.of(clientList);
  }

  public ClientResponseForm clientByName(ClientsByUsernameRequestForm form){
    Store store = storeRepository.findById(form.getStoreId()).get();
    List<Client> clientList = clientRepository.findAllByNameAndStore(form.getUsername(),store);
    return ClientResponseForm.of(clientList);
  }

  public ResponseForm valStamp(StampRequestForm form){
    Client client = clientRepository.findById(form.getClientId()).get();
    client.setStamp(client.getStamp()+form.getVal());
    clientRepository.save(client);
    return new ResponseForm("완료되었습니다.");
  }

}
