package com.ipv.su.udedis.dao;

import java.util.Set;

import redis.clients.jedis.Tuple;

public interface RedisDao {
	public Set<String> getKeys();
	public Set<Tuple> getKeyValueByPattern(String pattern);
	public String getValue(String key);
	
	public boolean deleteAll();
	public boolean deleteKey(String key);
	public boolean deleteByPattern(String pattern);
}
